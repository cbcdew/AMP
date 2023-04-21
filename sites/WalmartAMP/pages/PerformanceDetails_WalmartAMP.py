from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sites.WalmartAMP.pages.SeatMap_WalmartAMP import SeatMap_WalmartAMP
from utilities.BaseUtilities import BaseUtilities


class PerformanceDetails_WalmartAMP:
    # define selectors elements
    sel_ConfirmPage = (By.XPATH, "(//div[contains(string(),'Performance Details')]) [1]")
    eBuyTicketsButton = (By.XPATH, "(//button[contains(string(),'Buy Tickets')]) [1]")
    # text will be replaced at runtime
    sel_ConfirmArtistName = [By.XPATH, f"(//div[contains(string(),'{BaseUtilities.txt_ToReplace}')]) [1]"]
    artistName = ""


    def __init__(self, base, artistName):
        self.base = base
        self.driver = base.getDriver()
        self.artistName = artistName


    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPage, 5)
        self.confirm_ArtistName(self.artistName)


    def confirm_ArtistName(self, artistName):
        # this takes some elements and replaces some text part with the input
        self.base.confirm_ElementOnPage_AfterReplacingText(self.sel_ConfirmArtistName, artistName)
        '''        
                try:
                    self.sel_ConfirmArtistName[1].replace(BaseUtilities.txt_ToReplace, artistName)
                    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.sel_ConfirmArtistName))
                    self.driver.find_element(*self.sel_ConfirmArtistName).is_displayed()
                except Exception as e:
                    print(f"error confirm_ArtistName element_to_be_clickable failed: \n{str(e)}")
        '''

    def clickBuyTicketsButton_gotoPage_SeatMap_WalmartAMP(self, artistName):
        self.base.goTo_PageBySel(self.eBuyTicketsButton, 10)
        page = SeatMap_WalmartAMP(self.base, artistName)
        page.confirm_OnPage()
        return page

