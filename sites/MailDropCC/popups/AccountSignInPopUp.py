from selenium.webdriver.common.by import By


class AccountSignInPopUp:
    # define selectors elements
    sel_ConfirmPopUp = (By.XPATH, "(// div[contains(@class , 'font-normal') and contains(text(), 'Sign In')])[1]")

    sel_InputUsername = (By.XPATH, "(//input[contains(@id, 'mantine-')]) [1]")
    sel_InputPassword = (By.XPATH, "(//input[contains(@id, 'mantine-')]) [2]")
    sel_ButtonSignIn = (By.XPATH, "(//button[contains(string(), 'Sign In')]) [1]")
    txt_Username = "jane_doe_thevirtualwild@maildrop.cc"
    txt_Password = "thevirtualwild"

    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()

    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPopUp, 5)

    def signIn(self):
        # enter input data
        self.driver.find_element(self.sel_InputUsername).send_keys(self.txt_Username)
        self.driver.find_element(self.sel_InputPassword).send_keys(self.txt_Password)

        # click SignIn button
        self.driver.find_element(self.sel_ButtonSignIn).click()
        # self.driver.implicitly_wait(5)
