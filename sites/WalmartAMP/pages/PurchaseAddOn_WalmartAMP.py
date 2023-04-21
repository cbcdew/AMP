from selenium.webdriver.common.by import By

from sites.WalmartAMP.pages.Cart_WalmartAMP import Cart_WalmartAMP

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseUtilities import BaseUtilities


class PurchaseAddOn_WalmartAMP:
    # define selectors elements
    sel_ConfirmPage = (By.XPATH, "//strong[contains(string(),'Purchase')]")
    sel_OptionButton = (By.XPATH, "//div[contains(@id, 'headlessui-disclosure-panel')] //div[contains(@class, 'items-center justify-between gap')] //button[contains(@class, 'cursor-pointer items-center justify-center rounded-full border-none')] //*[name()='svg']")
    sel_GoToCartButton = (By.XPATH, "//button[contains(text(),'Go To Cart')]")

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


    def process_Click(self, sel, linkIdx, cnt):
        idx = 1
        while idx <= cnt:
            self.base.click_ElementByAddingIndex(sel, linkIdx)
            idx = idx + 1

    def click_LawnChairRental_Minus(self, cnt):
        self.process_Click(self.sel_OptionButton, 1, cnt)

    def click_LawnChairRental_Plus(self, cnt):
        self.process_Click(self.sel_OptionButton, 2, cnt)

    def click_FastTrack_Minus(self, cnt):
        self.process_Click(self.sel_OptionButton, 3, cnt)

    def click_FastTrack_Plus(self, cnt):
        self.process_Click(self.sel_OptionButton, 4, cnt)

    def click_PremierReservedParking_Minus(self, cnt):
        self.process_Click(self.sel_OptionButton, 5, cnt)

    def click_PremierReservedParking_Plus(self, cnt):
        self.process_Click(self.sel_OptionButton, 6, cnt)


    def click_GoToCartButton_gotoPage_Cart_WalmartAMP(self):
        self.base.goTo_PageBySel(self.sel_GoToCartButton, 5)
        page = Cart_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page



