import time

import pytest

from sites.WalmartAMP.components.HeaderMenu_WalmartAMP import HeaderMenu_WalmartAMP
from sites.WalmartAMP.objects.CustObj import CustObj
from sites.WalmartAMP.pages.AccountSignedIn_WalmartAMP import AccountSignedIn_WalmartAMP
from sites.WalmartAMP.pages.Home_WalmartAMP import Home_WalmartAMP
from utilities.BaseUtilities import BaseUtilities
from utilities.TestUtilities import TestUtilities

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
class Test_SeatMap_UI():

    @pytest.mark.SeatMap_UI
    def test_scaling(self, driver):
        testUtilities = TestUtilities(driver)
        base = testUtilities.base
        # config test
        custObj = CustObj()
        custObj.numOfPerfs = 1
        custObj.seatsToBuy_Regular = 0
        custObj.seatsToBuy_WheelChair = 1
        custObj.seatsToBuy_Companion = 1
        custObj.get_SeatsTotalNeeded()
        custObj.createList_AllSeatTypes()
        seatMap = testUtilities.init_GoTo_SeatMap(custObj)
        if seatMap is not None:
            #when first loading into the seat map, the zoom level should be fully zoomed out, scale(1)
            seatMap.checkScale(1)

            #maximum zoom / "zoomed in" state should be scale(20)
            seatMap.scaleToMax()
            seatMap.checkScale(20)

            #minimum zoom / "zoomed out" state should be scale(1) and should recenter the map
            seatMap.click_RotateButton()
            seatMap.checkScale(1)
            seatMap.checkCentered()

            #individual seats should be revealed once user has zoomed to scale(2.5)
            seatMap.click_Section_ByCustObj(custObj)
            seatMap.checkScaleAtLeast(2.5)
            seatMap.check_Seats_Visable()

            #when user clicks on an available section, it should automatically zoom in on that section using the focal point in the center of that section to scale(3)
            seatMap.click_Section_ByCustObj(custObj)
            seatMap.checkScale(3)

