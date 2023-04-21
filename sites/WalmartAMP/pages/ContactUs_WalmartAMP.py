from selenium.webdriver.common.by import By


class ContactUs_WalmartAMP:
    # define selectors elements
    sel_ConfirmPage = (By.XPATH, "(//div[contains(string(),'Contact Us')]) [1]")

    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()

    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPage, 5)
