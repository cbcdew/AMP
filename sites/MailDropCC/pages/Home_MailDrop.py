from selenium.webdriver.common.by import By

from sites.MailDropCC.pages.InBox_MailDrop import InBox_MailDrop


class Home_MailDrop:
    # define selectors elements
    sel_ConfirmPage = (By.XPATH, "(//input[@placeholder='view-this-mailbox'])[1]")

    sel_InputUsername = (By.XPATH, "(//input[@placeholder='view-this-mailbox'])[1]")
    buttonViewMail = (By.XPATH, "(//button[@type='submit'])[1]")
    txt_Username = "jane_doe_thevirtualwild"

    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()

    def goto_HomePageURL(self):
        # maximize window
        self.driver.maximize_window()
        # goto Home page
        pageHome = "https://maildrop.cc/"
        self.driver.get(pageHome)
        # check for hijacking...
        if (pageHome == self.driver.current_url):
            print("current url is correct: ", self.driver.current_url)
            print("page title is:", self.driver.title)
        else:
            print("expected url is : ", pageHome)
            print("page has been hijacked to: ", self.driver.current_url)
        self.confirm_OnPage()

    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPage, 5)

    def click_buttonViewMail(self):
        self.base.goTo_PageBySel(self.buttonViewMail, 5)
        page = InBox_MailDrop(self.base)
        return page
