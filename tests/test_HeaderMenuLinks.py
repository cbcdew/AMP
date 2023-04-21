import time

import pytest

from sites.WalmartAMP.components.HeaderMenu_WalmartAMP import HeaderMenu_WalmartAMP
from sites.WalmartAMP.pages.AccountSignedIn_WalmartAMP import AccountSignedIn_WalmartAMP
from sites.WalmartAMP.pages.Home_WalmartAMP import Home_WalmartAMP
from utilities.BaseUtilities import BaseUtilities

'''
NOTES:
selector examples:
//div[contains(@style, 'scale')]
//p[contains(string(), 'Seat')]
pytest:
- pytest file names should start with "test_" as in "test_HomePage"
- in pytest all code must be in methods like: def test_sometest:
- pytest methods should start with "test_" as in "test_gotoHomePage"
- pytest methods should contain logical grouping names
-- cmd line: py.test runs all test in current dir
-- cmd line: 
py.test -v=verbose -s=show internal print() to console values -k=run only methods that contain "GoToPage"
-- cmd line: py.test -v -s -k GoToHomePage
-- cmd line: py.test -v -s -m GoToAPage
'''


@pytest.mark.usefixtures("driver")
class Test_HomePageMenuLinks():

    @pytest.mark.TopMenu
    def test_GoTo_HomePageByTopLeftSel(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        headerMenu.click_ele_Home()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_About_WhoWeAre(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        whoweare = headerMenu.click_ele_WhoWeAre()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_About_Employment(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        employment = headerMenu.click_ele_Employment()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_About_PerformanceArchive(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        productionArchive = headerMenu.click_ele_PerformanceArchive()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_About_ContactUs(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        contactUs = headerMenu.click_ele_ContactUs()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_Venue_Rentals(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        rentals = headerMenu.click_ele_Rentals()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_Venue_Gallery(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        gallery = headerMenu.click_ele_Gallery()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_Venue_Maps(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        maps = headerMenu.click_ele_Maps()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_Venue_Policies(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        policies = headerMenu.click_ele_Policies()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_Support_ClubAMP(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        clubAMP = headerMenu.click_ele_ClubAMP()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_Support_CorporateSponsors(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        corporateSponsors = headerMenu.click_ele_CorporateSponsors()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_Calendar(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        calendar = headerMenu.click_ele_Calendar()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_Cart(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        cart = headerMenu.click_ele_Cart()
        time.sleep(2)

    @pytest.mark.TopMenu
    def test_GoTo_AccountAndSignIn(self, driver):
        baseAMP = BaseUtilities(driver)
        homeAMP = Home_WalmartAMP(baseAMP)
        homeAMP.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(baseAMP)
        signinPopUp = headerMenu.click_ele_AccountNotLoggedIn()
        signinPopUp.signIn()

        # don't need to click to goto this page, should already be there after signing in...
        # signedIn = headerMenu.click_ele_AccountLoggedIn()
        signedIn = AccountSignedIn_WalmartAMP(baseAMP)
        time.sleep(2)
