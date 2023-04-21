from os import environ

import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# RUN LOCAL
@pytest.fixture(scope='function')
def driver(request):
    # firefox driver
    # brower = webdriver.Firefox(firefox_options=fireFoxOptions)
    options = Options()
    options.headless = False
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    drvr = webdriver.Firefox(executable_path=r'C:\\geckodriver\\geckodriver.exe', options=options)

    '''
    # chrome driver
    self.serviceObj = Service("C:\\chromedriver\\chromedriver.exe")
    options = Options()
    options.headless = False
    #drvr = webdriver.Chrome(service=self.serviceObj, options=options)
    drvr = webdriver.Chrome(service=self.serviceObj)
    '''
    yield drvr

    drvr.close()


# RUN REMOTE
@pytest.fixture(scope='function')
def driver__(request):
    desired_caps = {}

    build = "WalmartAMP"
    tunnel_id = environ.get('TUNNEL', False)
    username = "charleskellywheeler"
    access_key = "EV7uUUw8E2z7j938XJuLLM2Y4IcvOIwZS4QAl7WGDgV4lV7br3"

    drvr = {
        "browserName": "Chrome",
        "browserVersion": "111.0",
        "LT:Options": {
            "username": username,
            "accessKey": access_key,
            "geoLocation": "US",
            "video": True,
            "platformName": "Windows 10",
            "timezone": "Chicago",
            "build": build,
            "project": f"{build}-Testing",
            "name": f"{build}-Testing",
            "console": "warn",
            "w3c": True,
            "plugin": "python-pytest"
        }
    }

    desired_caps.update(drvr)
    test_name = request.node.name

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    desired_caps['name'] = test_name
    desired_caps['video'] = True
    desired_caps['visual'] = True
    desired_caps['network'] = True
    desired_caps['console'] = True
    caps = {"LT:Options": desired_caps}

    executor = RemoteConnection(selenium_endpoint)
    drvr = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=caps
    )
    
    yield drvr

    def fin():
        # drvr.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else
        # "failed").lower()))
        if request.node.rep_call.failed:
            drvr.execute_script("lambda-status=failed")
        else:
            drvr.execute_script("lambda-status=passed")
            drvr.quit()

    request.addfinalizer(fin)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
