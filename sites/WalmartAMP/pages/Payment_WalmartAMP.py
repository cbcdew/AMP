from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Payment_WalmartAMP:
    # define selectors elements
    sel_ConfirmPage = (By.XPATH, "//strong[contains(string(),'Complete')]")

    sel_Input_CardNo = (By.XPATH, "//input[@id='cardNumber']")
    sel_Input_CVV = (By.XPATH, "//input[@id='CVV']")
    sel_Month = (By.XPATH, "//select[@id='ddlExpirationMonth']")
    sel_Year = (By.XPATH, "//select[@id='ddlExpirationYear']")

    sel_ButtonProcess = (By.XPATH, "// div[contains(text(), 'Ticket Delivery')]")
    # sel_iFrame = (By.TAG_NAME, "iframe")
    sel_iFrame = (By.XPATH, "iframe[id='embedded-iframe']")


    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()


    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPage, 5)


    def click_ProcessButton(self):
        self.base.click_ElementOnPage(self.sel_ButtonProcess)


    def enter_CCInfo(self):
        iframe = self.driver.find_element(*self.sel_Frame)
        self.driver.switch_to.frame(iframe)
        # enter input data
        self.driver.find_element(self.sel_Input_CardNo).send_keys(self.base.custObj.txt_CC)
        self.driver.find_element(self.sel_Input_CVV).send_keys(self.base.custObj.txt_CVV)
        self.select_FromDropDown(self.sel_Month, self.base.custObj.txt_Month)
        self.select_FromDropDown(self.sel_Year, self.base.custObj.txt_Year)


    def select_FromDropDown(self, sel, text):
        # identify dropdown with Select class
        sel = Select(self.driver.find_element(sel))
        # select by select_by_visible_text() method
        sel.select_by_visible_text(text)

'''
# to identify a cell , row 3 and column 2
c = driver.find_element_by_xpath ("//*[@class= 'spTable']/tbody/tr[3]/td[2]")'''

