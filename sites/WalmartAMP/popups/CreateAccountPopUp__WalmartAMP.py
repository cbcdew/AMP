import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseUtilities import BaseUtilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class CreateAccountPopUp_WalmartAMP:
    # define selectors elements
    sel_ConfirmPopUp = (By.XPATH, "(// div[contains(@class , 'font-normal') and contains(text(), 'Create an Account')]) [1]")

    sel_InputFirstName = (By.XPATH, "//input[contains(@name, 'firstName')]")
    sel_InputLastName = (By.XPATH, "//input[contains(@name, 'lastName')]")
    sel_InputEmail = (By.XPATH, "//input[contains(@name, 'email')]")
    sel_InputPassword = (By.XPATH, "//input[contains(@name, 'password')]")
    sel_InputPasswordRepeat = (By.XPATH, "//input[contains(@name, 'passwordRepeat')]")
    sel_InputPhoneNumber = (By.XPATH, "//input[contains(@name, 'phoneNumber')]")
    sel_InputAddr1 = (By.XPATH, "//input[contains(@name, 'street1')]")
    sel_InputAddr2 = (By.XPATH, "//input[contains(@name, 'street2')]")
    sel_InputCity = (By.XPATH, "//input[contains(@name, 'city')]")
    sel_State1 = (By.XPATH, "//input[contains(@placeholder, 'STATE')]")
    #sel_State2 = (By.XPATH, f"//*[contains(string(), '{BaseUtilities.txt_ToReplace}')]")
    sel_State2 = (By.XPATH, f"//*[contains(string(), '{BaseUtilities.txt_ToReplace}')]")
    sel_InputZip = (By.XPATH, "//input[contains(@name, 'postalCode')]")
    sel_InputAgree = (By.XPATH, "//input[contains(@name, 'comments')]")
    sel_ButtonSubmit = (By.XPATH, "(//button[contains(string(), 'Submit')]) [1]")
    sel_SignInError = (By.XPATH, "//div[contains(@id, 'error']")
    sel_CreateAccount = (By.XPATH, "//div[contains(text(),'CREATE AN ACCOUNT')]")


    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()


    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPopUp, 5)


    def fillData(self):
        # enter input data
        self.driver.find_element(*self.sel_InputFirstName).send_keys(self.base.custObj.txt_FirstName)
        self.driver.find_element(*self.sel_InputLastName).send_keys(self.base.custObj.txt_LastName)
        self.driver.find_element(*self.sel_InputEmail).send_keys(self.base.custObj.txt_Email)
        self.driver.find_element(*self.sel_InputPassword).send_keys(self.base.custObj.txt_Password)
        self.driver.find_element(*self.sel_InputPasswordRepeat).send_keys(self.base.custObj.txt_Password)
        self.driver.find_element(*self.sel_InputPhoneNumber).send_keys(self.base.custObj.txt_PhoneNumber)
        self.driver.find_element(*self.sel_InputAddr1).send_keys(self.base.custObj.txt_Addr1)
        self.driver.find_element(*self.sel_InputAddr2).send_keys(self.base.custObj.txt_Addr2)
        self.driver.find_element(*self.sel_InputCity).send_keys(self.base.custObj.txt_City)
        self.base.click_ElementOnPage(self.sel_State1)
        ele_State1 = self.driver.find_element(*self.sel_State1)
        # for testing I was using TX which is currently the 54th element in the dropdown
        idxClick = 54
        while idxClick >= 0:
            ele_State1.send_keys(Keys.DOWN)
            idxClick -= 1
        ele_State1.send_keys(Keys.RETURN)
        # ele_State1 = self.base.click_ElementOnPage(self.sel_State1)

        #ele_state = self.driver.find_element(*self.sel_State1)
        self.driver.find_element(*self.sel_InputZip).send_keys(self.base.custObj.txt_Zip)
        self.base.click_ElementOnPage(self.sel_InputAgree)


    def submitData(self):
        # click Submit button
        self.base.click_ElementOnPage(self.sel_ButtonSubmit)


    def getExists_SignIn_Error(self):
        sts = self.base.confirm_ElementOnPage(self.sel_SignInError)
        return sts


