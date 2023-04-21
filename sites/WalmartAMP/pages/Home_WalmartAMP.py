from selenium.webdriver.common.by import By


class Home_WalmartAMP:
    # define selectors elements
    sel_ConfirmPage = (By.XPATH, "(// div[contains( @class , 'mantine-Carousel-root')]) [1]")

    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()

    def goto_HomePageURL(self):
        # maximize window
        self.driver.maximize_window()
        # goto Home page
        pageAMPHome = "https://wacamp-amp-web-git-development-the-virtual-wild.vercel.app/"
        self.driver.get(pageAMPHome)
        # check for hijacking...
        if (pageAMPHome == self.driver.current_url):
            pass
            # print("current url is correct: ", self.driver.current_url)
            # print("page title is:", self.driver.title)
        else:
            pass
            # print("expected url is : ", pageAMPHome)
            # print("page has been hijacked to: ", self.driver.current_url)
        self.confirm_OnPage()

    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPage, 5)
