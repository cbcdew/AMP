from selenium.webdriver.common.by import By


class ADASeatingPopUp_WalmartAMP:
    # define selectors elements
    sel_ConfirmPopUp = (By.XPATH, "( //div[contains(@class , 'font-normal') and contains(text(), 'ADA Seating')] ) [1]")
    sel_ButtonContinue = (By.XPATH, "(//button[contains(string(), 'Continue')]) [1]")

    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()


    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPopUp, 5)

        # click Continue button
    def click_ContinueButton(self):
            self.driver.find_element(*self.sel_ButtonContinue).click()

