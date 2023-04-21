import time

from selenium.webdriver.common.by import By

from sites.WalmartAMP.pages.Payment_WalmartAMP import Payment_WalmartAMP
from sites.WalmartAMP.popups.AccountSignInPopUp__WalmartAMP import AccountSignInPopUp_WalmartAMP


class Cart_WalmartAMP:
    # define selectors elements
    sel_ConfirmPage = (By.XPATH, "(//div[contains(string(),'Cart')]) [1]")
    sel_ButtonCheckOut = (By.XPATH, "//button[contains(string(),'Checkout')]")
    sel_XButton_InCart = [By.XPATH, "//button[contains(@class, 'mantine-UnstyledButton-root')] //*[contains(name(),'svg') and contains(@class, 'icon')]"]

    # Review - //strong[contains(text(),'Review')]
    # Checkout button - //button[contains(text(),'Checkout')]
    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()

    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPage, 5)


    def click_CheckOutButton_gotoPage_Payment_WalmartAMP(self):
        self.base.click_ElementOnPage(self.sel_ButtonCheckOut)

        time.sleep(2)
        # signinPopUp
        signinPopUp = AccountSignInPopUp_WalmartAMP(self.base)
        time.sleep(1)
        signinPopUp.signIn()

        payment = Payment_WalmartAMP(self.base)
        payment.confirm_OnPage()
        return payment

    def removeSeats_from_Cart(self):
        eleList_X = []
        eleList_X = self.base.get_ElementsOnPage(self.sel_XButton_InCart)
        maxX = len(eleList_X)
        idxX = maxX - 1
        while (idxX >= 0):
            self.base.click_ElementOnPage(eleList_X[idxX])
            time.sleep(1)
            idxX -= 1


