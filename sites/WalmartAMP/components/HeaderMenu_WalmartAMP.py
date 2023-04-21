from selenium.webdriver.common.by import By

from sites.WalmartAMP.pages.AccountSignedIn_WalmartAMP import AccountSignedIn_WalmartAMP
from sites.WalmartAMP.pages.Calendar_WalmartAMP import Calendar_WalmartAMP
from sites.WalmartAMP.pages.Cart_WalmartAMP import Cart_WalmartAMP
from sites.WalmartAMP.pages.ClubAMP_WalmartAMP import ClubAMP_WalmartAMP
from sites.WalmartAMP.pages.ContactUs_WalmartAMP import ContactUs_WalmartAMP
from sites.WalmartAMP.pages.CorporateSponsors_WalmartAMP import CorporateSponsors_WalmartAMP
from sites.WalmartAMP.pages.Employment_WalmartAMP import Employment_WalmartAMP
from sites.WalmartAMP.pages.Gallery_WalmartAMP import Gallery_WalmartAMP
from sites.WalmartAMP.pages.Home_WalmartAMP import Home_WalmartAMP
from sites.WalmartAMP.pages.Maps_WalmartAMP import Maps_WalmartAMP
from sites.WalmartAMP.pages.PerformanceArchive_WalmartAMP import PerformanceArchive_WalmartAMP
from sites.WalmartAMP.pages.Policies_WalmartAMP import Policies_WalmartAMP
from sites.WalmartAMP.pages.Rentals_WalmartAMP import Rentals_WalmartAMP
from sites.WalmartAMP.pages.WhoWeAre_WalmartAMP import WhoWeAre_WalmartAMP
from sites.WalmartAMP.popups.AccountSignInPopUp__WalmartAMP import AccountSignInPopUp_WalmartAMP


class HeaderMenu_WalmartAMP:
    # define selectors elements
    sel_Home = (By.XPATH, "(//img[@alt='amp-logo']) [1]")

    sel_About = (By.XPATH, "(//button[contains(string(), 'About')]) [1]")
    sel_WhoWeAre = (By.XPATH, "(//a[contains(string(), 'Who We Are')]) [1]")
    sel_Employment = (By.XPATH, "(//a[contains(string(), 'Employment')]) [1]")
    sel_PerformanceArchive = (By.XPATH, "(//a[contains(string(), 'Performance Archive')]) [1]")
    sel_ContactUs = (By.XPATH, "(//a[contains(string(), 'Contact Us')]) [1]")

    sel_Venue = (By.XPATH, "(//button[contains(string(), 'Venue')]) [1]")
    sel_Rentals = (By.XPATH, "(//a[contains(string(), 'Rentals')]) [1]")
    sel_Gallery = (By.XPATH, "(//a[contains(string(), 'Gallery')]) [1]")
    sel_Maps = (By.XPATH, "(//a[contains(string(), 'Maps')]) [1]")
    sel_Policies = (By.XPATH, "(//a[contains(string(), 'Policies')]) [1]")

    sel_Support = (By.XPATH, "(//button[contains(string(), 'Support')]) [1]")
    sel_ClubAMP = (By.XPATH, "(//a[contains(string(), 'Club AMP')]) [1]")
    sel_CorporateSponsors = (By.XPATH, "(//a[contains(string(), 'Corporate Sponsors')]) [1]")

    sel_Calendar = (By.XPATH, "(//a[contains(string(), 'Calendar')]) [1]")
    sel_Cart = (By.XPATH, "(// a[contains(string(), 'Cart')]) [1]")

    sel_AccountNotLoggedIn = (By.XPATH, "(//a[contains(string(), 'Account')]) [1]")
    sel_AccountLoggedIn = (By.XPATH, "(//a[contains(string(), 'Hi,')]) [1]")

    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()

    def click_ele_Home(self):
        self.base.goTo_PageBySel(HeaderMenu_WalmartAMP.sel_Home, 5)
        page = Home_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_WhoWeAre(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_About, HeaderMenu_WalmartAMP.sel_WhoWeAre, 5)
        page = WhoWeAre_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_Employment(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_About, HeaderMenu_WalmartAMP.sel_Employment, 5)
        page = Employment_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_PerformanceArchive(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_About, HeaderMenu_WalmartAMP.sel_PerformanceArchive, 5)
        page = PerformanceArchive_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_ContactUs(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_About, HeaderMenu_WalmartAMP.sel_ContactUs, 5)
        page = ContactUs_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_Rentals(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_Venue, HeaderMenu_WalmartAMP.sel_Rentals, 5)
        page = Rentals_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_Gallery(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_Venue, HeaderMenu_WalmartAMP.sel_Gallery, 5)
        page = Gallery_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_Maps(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_Venue, HeaderMenu_WalmartAMP.sel_Maps, 5)
        page = Maps_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_Policies(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_Venue, HeaderMenu_WalmartAMP.sel_Policies, 5)
        page = Policies_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_ClubAMP(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_Support, HeaderMenu_WalmartAMP.sel_ClubAMP, 5)
        page = ClubAMP_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_CorporateSponsors(self):
        self.base.goTo_PageBy2MenuSels(HeaderMenu_WalmartAMP.sel_Support, HeaderMenu_WalmartAMP.sel_CorporateSponsors,5 )
        page = CorporateSponsors_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_Calendar(self):
        self.base.goTo_PageBySel(HeaderMenu_WalmartAMP.sel_Calendar, 5)
        page = Calendar_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_Cart(self):
        self.base.goTo_PageBySel(HeaderMenu_WalmartAMP.sel_Cart, 5)
        page = Cart_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_AccountNotLoggedIn(self):
        self.base.goTo_PageBySel(HeaderMenu_WalmartAMP.sel_AccountNotLoggedIn, 5)
        page = AccountSignInPopUp_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page

    def click_ele_AccountLoggedIn(self):
        self.base.goTo_PageBySel(HeaderMenu_WalmartAMP.sel_AccountLoggedIn, 5)
        page = AccountSignedIn_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page
