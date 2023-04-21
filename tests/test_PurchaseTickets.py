import time

import pytest

from sites.WalmartAMP.components.HeaderMenu_WalmartAMP import HeaderMenu_WalmartAMP
from sites.WalmartAMP.objects.CustObj import CustObj
from sites.WalmartAMP.objects.SeatObj import SeatObj
from sites.WalmartAMP.pages.AccountSignedIn_WalmartAMP import AccountSignedIn_WalmartAMP
from sites.WalmartAMP.pages.Home_WalmartAMP import Home_WalmartAMP
from sites.WalmartAMP.pages.PurchaseAddOn_WalmartAMP import PurchaseAddOn_WalmartAMP
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
'''
LT  --user charleskellywheeler@gmail.com --key Fpufvq36uqWszBTJ15AhYE4aLlPPJCR7phVVmDwuY9yANOlkl1
set LT_USERNAME="YOUR_USERNAME" set LT_ACCESS_KEY="YOUR ACCESS KEY"


'''


class Test_PurchaseTickets:

    @pytest.mark.usefixtures("driver")
    def test_SinglePerf_PurchaseTicket_Regular(self, driver):
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
            seatObj = custObj.seatObjList_AllSeatsNeeded[0]
            sts = seatMap.click_Section_ByCustObj(custObj)
            if sts:
                sts = seatMap.click_ValidatedSeats_ByCustObj(custObj)
                if sts:
                    if(custObj.seatsToBuy_WheelChair > 0) or (custObj.seatsToBuy_Companion > 0):
                        aDASeatingPopUp = seatMap.click_AddToCartButton_gotoPage__ADASeatingPopUp_WalmartAMP()
                        time.sleep(.5)
                        aDASeatingPopUp.click_ContinueButton()
                    if(seatMap.getExists_InvalidSession_PleaseRemoveTheHighlightedSeats()):
                        # need to remove seats from pre-cart list, then continue to search...
                        time.sleep(1)
                        seatMap.removeSeats_from_PreCart()
                        time.sleep(1)
                    else:
                        # continue purchase...
                        # should already be on this page...
                        purchaseAddOn = PurchaseAddOn_WalmartAMP(base, custObj.txt_ArtistName)
                        purchaseAddOn.click_LawnChairRental_Plus(1)
                        purchaseAddOn.click_FastTrack_Plus(1)
                        purchaseAddOn.click_PremierReservedParking_Plus(1)
                        cart = purchaseAddOn.click_GoToCartButton_gotoPage_Cart_WalmartAMP()

                        # Note: if cust is not logged in then they will get logged in
                        #payment = cart.click_CheckOutButton_gotoPage_Payment_WalmartAMP()
                        #payment.enter_CCInfo()
                        #payment.click_ProcessButton()
                        #continue purchase
                        time.sleep(2)
                        cart.removeSeats_from_Cart()
                        time.sleep(2)


