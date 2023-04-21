import inspect
import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from sites.WalmartAMP.objects.CustObj import CustObj


class BaseUtilities:
    txt_ToReplace = "~~~"
    txt_Plus = "plus"
    txt_Minus = "minus"

    def __init__(self, driver):
        self.driver = driver
        # enter input data
        self.custObj = CustObj()
        self.custObj.txt_CustName = "Jane Doe"
        self.custObj.txt_FirstName = "Jane"
        self.custObj.txt_LastName = "Doe"
        self.custObj.txt_Email = "jane_doe_thevirtualwild@maildrop.cc"
        self.custObj.txt_Password = "thevirtualwild"
        self.custObj.txt_PhoneNumber = "5125551212"
        self.custObj.txt_Addr1 = "123 Main St."
        self.custObj.txt_Addr2 = "Suite 1"
        self.custObj.txt_City = "Anywhere"

        self.custObj.txt_State = "TX"
        self.custObj.txt_Zip = "54321"

        self.custObj.txt_CC = "4484070000000000"
        self.custObj.txt_CCMonth = "02"
        self.custObj.txt_CCYear = "2024"
        self.custObj.txt_CVV = "411"


    def getDriver(self):
        return self.driver


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


    def getShadowRootElement(self, element):
        ele = self.driver.execute_script("return arguments[0].shadowRoot", element)
        return ele


    def confirm_ElementOnPage(self, sel):
        sts = False
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(sel))
            self.driver.find_element(*sel).is_displayed()
            eleList = self.driver.find_elements(*sel)

            sts = True
        except Exception as e:
            print(f"error confirm_ElementOnPage failed: \n{str(e)}")
        finally:
            return sts


    def confirm_ElementOnPage_AfterReplacingText(self, sel, txt_ToReplace):
        sts = False
        try:
            txt_Sel = sel[1]
            txt_New = txt_Sel.replace(BaseUtilities.txt_ToReplace, txt_ToReplace)
            sel_New = [sel[0], txt_New]
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(sel_New))
            self.driver.find_element(*sel_New).is_displayed()
            sts = True
        except Exception as e:
            print(f"error goTo_PageBySel element_to_be_clickable failed: \n{str(e)}")
        finally:
            return sts


    def getText_ElementOnPage_AfterReplacingText(self, sel, txt_ToReplace):
        text = None
        try:
            txt_Sel = sel[1]
            txt_New = txt_Sel.replace(BaseUtilities.txt_ToReplace, txt_ToReplace)
            sel_New = [sel[0], txt_New]
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(sel_New))
            text = self.driver.find_element(*sel_New).text
            return text
        except Exception as e:
            print(f"error goTo_PageBySel element_to_be_clickable failed: \n{str(e)}")
        finally:
            return text


    def confirm_OnPage(self, confirm, sec):
        sts = False
        try:
            WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(confirm))
            self.driver.find_element(*confirm).is_displayed()
            sts = True
        except Exception as e:
            self.driver.close()
        finally:
            return sts


    def click_ElementByAddingIndex(self, sel, idx):
        sts = False
        sel_New = None
        try:
            txt_Sel = f"( {sel[1]} ) [{idx}]"
            sel_New = [sel[0], txt_Sel]
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(sel_New)).click()
            sts = True
        except Exception as e:
            print(f"\n{str(e)}")
        finally:
            return sts


    def get_sel_AfterReplacingText(self, sel, txt_ToReplace):
        sel_New = None
        try:
            txt_Sel = sel[1]
            txt_New = txt_Sel.replace(BaseUtilities.txt_ToReplace, txt_ToReplace)
            sel_New = [sel[0], txt_New]
        except Exception as e:
            print(f"\n{str(e)}")
        finally:
            return sel_New


    def get_ElementsOnPage(self, sel):
        eleList = []
        try:
            eleList = self.driver.find_elements(*sel)
        except Exception as e:
            print(f"\n{str(e)}")
        finally:
            return eleList


    def get_ElementsOnPage_AfterReplacingText(self, sel, txt_ToReplace):
        eleList = []
        try:
            txt_Sel = sel[1]
            txt_New = txt_Sel.replace(BaseUtilities.txt_ToReplace, txt_ToReplace)
            sel_New = [sel[0], txt_New]
            eleList = self.driver.find_elements(*sel_New)
        except Exception as e:
            print(f"\n{str(e)}")
        finally:
            return eleList


    def click_ElementOnPage_AfterReplacingText(self, sel, txt_ToReplace):
        sts = False
        try:
            txt_Sel = sel[1]
            txt_New = txt_Sel.replace(BaseUtilities.txt_ToReplace, txt_ToReplace)
            sel_New = [sel[0], txt_New]
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(sel_New)).click()
            sts = True
        except Exception as e:
            print(f"\n{str(e)}")
        finally:
            return sts


    def click_ElementOnPage(self, sel):
        sts = False
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(sel)).click()
            sts = True
        except Exception as e:
            print(f"\n{str(e)}")
        finally:
            return sts


    def click_SubElementOnPage(self, sel, sublink):
        sts = False
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(sel))
            element = self.driver.find_element(*sel)
            element.find_element(*sublink).click()
            sts = True
        except Exception as e:
            print(f"\n{str(e)}")
        finally:
            return sts

    def goTo_PageByClickingElementInList(self, sel_1, idx, sec):
        sel_New = None
        try:
            txt_Sel = f"( {sel_1[1]} ) [{idx}]"
            sel_New = [sel_1[0], txt_Sel]
            WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(sel_New)).click()
        except Exception as e:
            print(f"\n{str(e)}")

    def goTo_PageBySel(self, sel_1, sec):
        '''
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(sel_1))
            #WebDriverWait(self.driver, 5).until(EC.invisibility_of_element(sel_1))
        except Exception as e:
            print("error goTo_PageBySel invisibility_of_element failed:", sel_1, '\ne:', str(e))
        '''
        try:
            WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(sel_1)).click()
        except Exception as e:
            print(f"\n{str(e)}")


    def goTo_PageBy2MenuSels(self, sel_1, sel_2, sec):
        try:
            WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(sel_1)).click()
        except Exception as e:
            print(f"\n{str(e)}")
        try:
            WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(sel_2)).click()
        except Exception as e:
            print(f"\n{str(e)}")


    def select_BySel_ThenBySel_AfterReplacingText(self, sel1, sel2, txt):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(sel1)).click()
            sel2 = self.get_sel_AfterReplacingText(sel2, txt)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(sel1)).click()
        except Exception as e:
            print(f"\n{str(e)}")


    def select_By2MenuSels(self, sel_1, sel_2):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(sel_1)).click()
        except Exception as e:
            print(f"\n{str(e)}")
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(sel_2)).click()
        except Exception as e:
            print(f"\n{str(e)}")


    def closeDriver(self):
        self.driver.close()

    def quitDriver(self):
        self.driver.quit()

    def get_LetterByOffset(self, letter, offset):
        idx = ord(letter)
        idx = idx + offset
        return chr(idx)

    def get_IdxByLetterOffset(self, letter, offset):
        idx = ord(letter)
        idx = idx + offset
        return idx

