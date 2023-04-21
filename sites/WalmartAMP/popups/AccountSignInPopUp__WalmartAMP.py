import time

from selenium.webdriver.common.by import By

from sites.WalmartAMP.popups.CreateAccountPopUp__WalmartAMP import CreateAccountPopUp_WalmartAMP


class AccountSignInPopUp_WalmartAMP:
    # define selectors elements
    sel_ConfirmPopUp = (By.XPATH, "(// div[contains(@class , 'font-normal') and contains(text(), 'Sign In')]) [1]")

    sel_InputUsername = (By.XPATH, "(//input[contains(@id, 'mantine-')]) [1]")
    sel_InputPassword = (By.XPATH, "(//input[contains(@id, 'mantine-')]) [2]")
    sel_ButtonSignIn = (By.XPATH, "(//button[contains(string(), 'Sign In')]) [1]")

    # //div[@id='mantine-r2k-error']
    sel_SignInError = (By.XPATH, "//div[contains(@id, '-error')]")
    sel_CreateAccount = (By.XPATH, "//div[contains(text(),'CREATE AN ACCOUNT')]")


    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()


    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPopUp, 5)

    def signIn(self):
        # enter input data
        self.driver.find_element(*self.sel_InputUsername).send_keys(self.base.custObj.txt_Email)
        self.driver.find_element(*self.sel_InputPassword).send_keys(self.base.custObj.txt_Password)

        # click SignIn button
        self.driver.find_element(*self.sel_ButtonSignIn).click()
        time.sleep(2)
        if(self.getExists_SignIn_Error()):
            self.base.click_ElementOnPage(self.sel_CreateAccount)
            createAccount = CreateAccountPopUp_WalmartAMP(self.base)
            createAccount.confirm_OnPage()
            createAccount.fillData()
            createAccount.submitData()


    def getExists_SignIn_Error(self):
        sts = False
        eleList = self.base.get_ElementsOnPage(self.sel_SignInError)
        if(len(eleList) > 0):
            sts = True
        return sts

    '''
    def click_CreateAccount_gotoPage__CreateAccountPopUp_WalmartAMP(self):
        self.base.goTo_PageBySel(self.sel_CreateAccount, 5)
        createAccount = CreateAccountPopUp_WalmartAMP(self.base)
        createAccount.confirm_OnPage()
        return page

    '''
