import copy
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sites.WalmartAMP.objects.CustObj import CustObj
from sites.WalmartAMP.objects.SeatObj import SeatObj
from sites.WalmartAMP.objects.SelectedObj import SelectedObj
from sites.WalmartAMP.pages.PurchaseAddOn_WalmartAMP import PurchaseAddOn_WalmartAMP
from sites.WalmartAMP.popups.ADASeatingPopUp__WalmartAMP import ADASeatingPopUp_WalmartAMP
from utilities.BaseUtilities import BaseUtilities


class SeatMap_WalmartAMP(BaseUtilities):
    # define selectors elements
    sel_SectionToClick = [By.CSS_SELECTOR, f"#section-container-{BaseUtilities.txt_ToReplace}"]
    sel_Section = [By.XPATH, f"{BaseUtilities.txt_ToReplace}"]
    sel_Seat = [By.XPATH, f"{BaseUtilities.txt_ToReplace}"]
    sel_Seats_InSelected = [By.XPATH, "//div[contains(@class, 'flex items-center gap-4')]"]
    sel_SeatInfo_InSelected = [By.XPATH, f"( //div[contains(@class, 'flex items-center gap-4')] )[{BaseUtilities.txt_ToReplace}]"]

    sel_ButtonAddToCart = [By.XPATH, "//button[contains(string(), 'Add To Cart')]"]
    sel_ButtonRotate = [By.XPATH, "//img[contains(@alt,'rotate')]"]
    sel_ButtonPlus = [By.XPATH, "//img[contains(@alt,'zoom-in')]"]
    sel_ButtonMinus = [By.XPATH, "//img[contains(@alt,'zoom-out')]"]
    sel_InvalidSession_PleaseRemoveTheHighlightedSeats = [By.XPATH, "//div[contains(@class, 'sticky top-')] //*[contains(string(), 'Please remove the highlighted seats')]"]
    sel_XButton_InPreCart = [By.XPATH, "//button[contains(@class, 'mantine-UnstyledButton-root')] //*[contains(name(),'svg') and contains(@class, 'icon')]"]



    def __init__(self, base, artistName):
        self.log = self.getLogger()
        self.base = base
        self.driver = base.getDriver()
        self.artistName = artistName
        self.eleList_Seat_Available = []
        self.eleList_Seat_Regular_Available = []
        self.eleList_Seat_Wheelchair_Available = []
        self.eleList_Seat_Companion_Available = []
        self.Seats_Available = 0
        self.Seats_Regular_Available = 0
        self.Seats_Wheelchair_Available = 0
        self.Seats_Companion_Available = 0
        self.sel_ConfirmPage = (By.XPATH, f"(//div[contains(string(),'{self.artistName}')]) [1]")
        # text will be replaced at runtime
        self.sel_ConfirmArtistName = [By.XPATH, f"(//div[contains(string(),'{BaseUtilities.txt_ToReplace}')]) [1]"]

    def select_SeatInSelected_ByIndex(self, sel, selectedIdx):
        selectedObj = None
        try:
            txt_Sel = f"( {sel[1]} ) [{selectedIdx}]"
            sel_New = [sel[0], txt_Sel]

            # get row of data
            rowElement = self.driver.find_element(*sel_New)
            sectionIdxSM = self.base.getText_ElementOnPage_AfterReplacingText(self.sel_SeatInfo_InSelected, 2)
            rowLetter = self.base.getText_ElementOnPage_AfterReplacingText(self.sel_SeatInfo_InSelected, 4)
            seatIdx = self.base.getText_ElementOnPage_AfterReplacingText(self.sel_SeatInfo_InSelected, 6)
            selectedObj = SelectedObj(sectionIdxSM, rowLetter, seatIdx)

            return selectedObj
        except Exception as e:
            self.log.debug(f"\n{str(e)}")

    def validate_SeatInSelected(self):
        sts = False
        try:
            seatObj = self.base.custObj.get_LastSeatAdded()
            self.initData_AllSelectedSeats()
            selectedObj = self.select_SeatInSelected_ByIndex(self.base, self.sel_Seats_InSelected)

            if (seatObj.seatIdx == selectedObj.seatIdx) and (seatObj.sectionIdxSM == selectedObj.sectionIdxSM) and (
                    seatObj.rowLetter == selectedObj.rowLetter):
                sts = True
            return sts
        except Exception as e:
            self.log.debug(f"\n{str(e)}")

    def initData_AllSelectedSeats(self):
        self.eleList_Seats_InSelected = self.driver.find_elements(*self.sel_Seat_InSelected)
        self.Seats_InSelected_Max = len(self.eleList_Seats_InSelected)

    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPage, 15)
        self.confirm_ArtistName(self.artistName)
        time.sleep(5)
        self.initData_ForAllSeatsOnMap()


    def click_Section_ByCustObj(self, custObj):
        seatObj = custObj.seatObjList_AllSeatsNeeded[0]
        sts = self.base.click_ElementOnPage_AfterReplacingText(self.sel_SectionToClick, str(seatObj.sectionIdxSM))
        return sts


    def click_Section_BySeatObj(self, seatObj):
        sts = self.base.click_ElementOnPage_AfterReplacingText(self.sel_SectionToClick, str(seatObj.sectionIdxSM))
        return sts


    def click_ValidatedSeats_ByCustObj(self, custObj):
        sts = True
        idxSeats = 0
        maxSeats = len(custObj.seatObjList_AllSeatsNeeded)
        while (sts) and (idxSeats < maxSeats):
            # time.sleep(2)
            seatObj = custObj.seatObjList_AllSeatsNeeded[idxSeats]
            sts = self.click_Seat(seatObj)
            if sts:
                time.sleep(.20)
                sts = custObj.add_Seat(seatObj)
            idxSeats += 1
        return sts


    def click_RotateButton(self):
        sts = self.base.click_ElementOnPage(self.sel_ButtonRotate)
        return sts


    def click_AddToCart(self):
        sts = self.base.click_ElementOnPage(self.sel_ButtonAddToCart)
        return sts


    def getEle_SpecificSeatOnMap(self, seatObj):
        ele_Seat = None
        sel_New = self.base.get_sel_AfterReplacingText(self.sel_Seat, seatObj.seltxt_SpecificSeatOnMap)
        list_Seats = self.base.get_ElementsOnPage(sel_New)
        if(len(list_Seats) == 1):
            ele_Seat = list_Seats[0]
        return ele_Seat


    def getSel_SpecificSeatOnMap_bySeatType(self, seatObj):
        sel_New = self.base.get_sel_AfterReplacingText(self.sel_Seat, seatObj.seltxt_SpecificSeatOnMap_bySeatType)
        list_Seats = self.base.get_ElementsOnPage(sel_New)
        max = len(list_Seats)
        if (max == 0):
            sel_New = None
        return sel_New


    def getMax_SeatsInRowSection(self, seatObj):
        seatsInRowList = self.base.get_ElementsOnPage_AfterReplacingText(self.sel_Seat, seatObj.seltxt_SeatsInRow)
        seatsInRowMax = len(seatsInRowList)
        return seatsInRowMax


    def getSel_SpecificSeatOnMap(self, seatObj):
        sel_New = self.base.get_sel_AfterReplacingText(self.sel_Seat, seatObj.seltxt_SpecificSeatOnMap_bySeatType)
        list_Seats = self.base.get_ElementsOnPage(sel_New)
        max = len(list_Seats)
        if (max == 0):
            sel_New = None
        return sel_New


    def click_Seat(self, seatObj):
        sts = self.base.click_ElementOnPage_AfterReplacingText(self.sel_Seat, seatObj.seltxt_SpecificSeatOnMap)
        return sts


    def confirm_ArtistName(self, artistName):
        # this takes some elements and replaces some text part with the input
        self.base.confirm_ElementOnPage_AfterReplacingText(self.sel_ConfirmArtistName, artistName)


    def initData_ForAllSeatsOnMap(self):
        self.eleList_Seat_Available = self.driver.find_elements(*SeatObj.sel_Seat_Available)
        self.Seats_Available = len(self.eleList_Seat_Available)
        '''        
        self.eleList_Seat_Regular_Available = self.driver.find_elements(*SeatObj.sel_Seat_Regular_Available)
        self.Seats_Regular_Available = len(self.eleList_Seat_Regular_Available)
        self.eleList_Seat_Wheelchair_Available = self.driver.find_elements(*SeatObj.sel_Seat_Wheelchair_Available)
        self.Seats_Wheelchair_Available = len(self.eleList_Seat_Wheelchair_Available)
        self.eleList_Seat_Companion_Available = self.driver.find_elements(*SeatObj.sel_Seat_Companion_Available)
        self.Seats_Companion_Available = len(self.eleList_Seat_Companion_Available)
        '''


    def getList_SeatsAvailable(self, custObj, seatObj):
        eleList_ValidatedSeats = []
        tseatObj = copy.copy(seatObj)
        if custObj.seatsTotalNeeded <= self.Seats_Available:
            idxSection = 8
            minSection = 4
            tseatObj.sectionIdxSM = idxSection
            tseatObj.update_Info()
            while(idxSection >= minSection):
                eleList_SeatsInSection_Available = self.base.get_ElementsOnPage_AfterReplacingText(self.sel_Section, tseatObj.seltxt_SeatsInSection_Available)
                maxSeatsInSection = len(eleList_SeatsInSection_Available)
                if(custObj.seatsTotalNeeded <= maxSeatsInSection):
                    idxRow = ord("S")
                    minRow = ord("A")
                    tseatObj.rowLetter = chr(idxRow)
                    tseatObj.update_Info()
                    while( idxRow >= minRow):
                        eleList_SeatsInRow_Available = self.base.get_ElementsOnPage_AfterReplacingText(self.sel_Seat, tseatObj.seltxt_SeatsInRow_Available)
                        maxSeatsInRow = len(eleList_SeatsInRow_Available)
                        if (custObj.seatsTotalNeeded <= maxSeatsInRow):
                            eleList_Seat_Regular_Available = self.getList_InRow_SeatsAvailable_BySeatType(SeatObj.txt_SeatType_Regular_Available, tseatObj)
                            maxSeats_Regular_Available = len(eleList_Seat_Regular_Available)
                            eleList_Seat_Wheelchair_Available = self.getList_InRow_SeatsAvailable_BySeatType(SeatObj.txt_SeatType_Wheelchair_Available, tseatObj)
                            maxSeats_Wheelchair_Available = len(eleList_Seat_Wheelchair_Available)
                            eleList_Seat_Companion_Available = self.getList_InRow_SeatsAvailable_BySeatType(SeatObj.txt_SeatType_Companion_Available, tseatObj)
                            maxSeats_Companion_Available = len(eleList_Seat_Companion_Available)

                            if((custObj.seatsToBuy_WheelChair <= maxSeats_Wheelchair_Available) and
                                (custObj.seatsToBuy_Companion <= maxSeats_Companion_Available) and
                                (custObj.seatsToBuy_Regular <= maxSeats_Regular_Available)):
                                # append lists...
                                eleList_ValidatedSeats += eleList_SeatsInRow_Available

                        idxRow -= 1
                        tseatObj.rowLetter = chr(idxRow)
                        tseatObj.update_Info()

                idxSection -= 1
                tseatObj.sectionIdxSM -= 1
                tseatObj.sectionIdxLG -= 1
                tseatObj.update_Info()
        '''
        eleList_Seats = []
        idxRowsWithSeats = 0
        maxRowsWithSeats = len(eleList_ValidatedSeats)
        while(idxRowsWithSeats < maxRowsWithSeats):
            eleList = self.driver.find_elements(*SeatObj.sel_Seat_Available)
            eleList_Seats += eleList
            idxRowsWithSeats += 1
        '''
        return eleList_ValidatedSeats




    def getList_InRow_SeatsAvailable_BySeatType(self, txt_SeatType, seatObj):
        eleList_Seats = []
        if(txt_SeatType == SeatObj.txt_SeatType_Regular_Available):
            eleList_Seats = self.base.get_ElementsOnPage_AfterReplacingText(self.sel_Section, seatObj.seltxt_SeatsInRow_Regular_Available)
        elif(txt_SeatType == SeatObj.txt_SeatType_Wheelchair_Available):
            eleList_Seats = self.base.get_ElementsOnPage_AfterReplacingText(self.sel_Section, seatObj.seltxt_SeatsInRow_Wheelchair_Available)
        elif(txt_SeatType == SeatObj.txt_SeatType_Companion_Available):
            eleList_Seats = self.base.get_ElementsOnPage_AfterReplacingText(self.sel_Section, seatObj.seltxt_SeatsInRow_Companion_Available)
        return eleList_Seats


    def getList_SeatsAvailable_BySeatType(self, custObj, eleList):
        # start with shortest list
        eleList_Seats = []
        if custObj.seatsToBuy_WheelChair > 0:
            if custObj.seatsToBuy_WheelChair <= self.Seats_Wheelchair_Available:
                eleList_Seats = eleList.find_elements(*SeatObj.sel_Seat_Wheelchair_Available)
                self.Seats_Wheelchair_Available = len(eleList_Seats)
                return self.eleList_Seats
        if custObj.seatsToBuy_Companion > 0:
            if custObj.seatsToBuy_Companion <= self.Seats_Companion_Available:
                eleList_Seats = eleList.find_elements(*SeatObj.sel_Seat_Companion_Available)
                self.Seats_Companion_Available = len(eleList_Seats)
                return self.eleList_Seats
        if custObj.seatsToBuy_Regular > 0:
            if custObj.seatsToBuy_Regular <= self.Seats_Regular_Available:
                eleList_Seats = eleList.find_elements(*SeatObj.sel_Seat_Regular_Available)
                self.Seats_Regular_Available = len(eleList_Seats)
                return self.eleList_Seats
        return eleList_Seats


    def check_Seats_Available(self, custObj):
        sts = False
        if custObj.seatsToBuy_Regular > 0:
            if custObj.seatsToBuy_Regular <= self.Seats_Regular_Available:
                sts = True
                return sts
        if custObj.seatsToBuy_WheelChair > 0:
            if custObj.seatsToBuy_WheelChair <= self.Seats_Wheelchair_Available:
                sts = True
                return sts
        if custObj.seatsToBuy_Companion > 0:
            if custObj.seatsToBuy_Companion <= self.Seats_Companion_Available:
                sts = True
                return sts
        return sts

    def getMax_Seats_Regular_Available(self):
        return self.Seats_Regular_Available

    def getMax_Seats_Wheelchair_Available(self):
        return self.Seats_Wheelchair_Available

    def getMax_Seats_Companion_Available(self):
        return self.Seats_Companion_Available

    def click_Seat_Regular_Available(self, seatIdx):
        sts = self.click_SectionAndSeatOnPage_ByIndex(self.sel_Seat_Regular_Available, seatIdx, self.txt_SeatType_Regular_Available)
        return sts

    def process_Validate_SeatsAvailable(self, custObj):
        sts = False
        # ckw
        seatObj = SeatObj()
        eleList_Seats = self.getList_SeatsAvailable(custObj, seatObj)
        #eleList_Seats = self.getList_SeatsAvailable_BySeatType(custObj, eleList_Seats)
        maxList_Seats = len(eleList_Seats)
        idxList_Seats = 0
        while ((idxList_Seats < maxList_Seats) and (sts == False)):
            if self.validate_SeatOnPage_ByIndex(custObj, eleList_Seats[idxList_Seats]):
                sts = True
                # sts = seatMap.validate_Seats_Available(custObj)
                # sts = seatMap.click_Seat_Regular_Available(idxList_Seats)
            idxList_Seats += 1
        return sts


    def process_Validate_SeatsAvailable_AndSelect(self, custObj):
        sts = False
        # ckw
        seatObj = SeatObj()
        eleList_Seats = self.getList_SeatsAvailable(custObj, seatObj)
        #eleList_Seats = self.getList_SeatsAvailable_BySeatType(custObj, eleList_Seats)
        maxList_Seats = len(eleList_Seats)
        idxList_Seats = 0
        while ((idxList_Seats < maxList_Seats) and (sts == False)):
            if self.validate_SeatOnPage_ByIndex_AndSelect(custObj, eleList_Seats[idxList_Seats]):
                sts = True
                # sts = seatMap.validate_Seats_Available(custObj)
                # sts = seatMap.click_Seat_Regular_Available(idxList_Seats)
            idxList_Seats += 1
        return sts


    def validate_SeatOnPage_ByIndex(self, custObj, ele_Seat):
        sts = False
        try:
            # cust = CustObj()
            # reset custObj selected values to 0
            custObj.resetSelected()
            #self.click_RotateButton()
            txt_Id = ele_Seat.get_attribute('id')
            txt_SeatType = ele_Seat.get_attribute('class')
            seatObj = SeatObj()
            seatObj.setup(txt_Id, txt_SeatType)
            sts = self.validate_AllSeatsNeeded_Found(custObj, seatObj)
        except Exception as e:
            self.log.debug(f"\n{str(e)}")
        return sts


    def validate_SeatOnPage_ByIndex_AndSelect(self, custObj, ele_Seat):
        sts = False
        try:
            # cust = CustObj()
            # reset custObj selected values to 0
            custObj.resetSelected()
            #self.click_RotateButton()
            txt_Id = ele_Seat.get_attribute('id')
            txt_SeatType = ele_Seat.get_attribute('class')
            seatObj = SeatObj()
            seatObj.setup(txt_Id, txt_SeatType)

            sts = self.validate_AllSeatsNeeded_Found(custObj, seatObj)
            if sts:
                sts = self.click_Section_ByCustObj(custObj)
                if sts:
                    idx_seatObjList_AllSeatsNeeded = 0
                    max_seatObjList_AllSeatsNeeded = len(custObj.seatObjList_AllSeatsNeeded)
                    while (sts) and (idx_seatObjList_AllSeatsNeeded < max_seatObjList_AllSeatsNeeded):
                        #time.sleep(2)
                        seatObj = custObj.seatObjList_AllSeatsNeeded[idx_seatObjList_AllSeatsNeeded]
                        sts = self.click_Seat(seatObj)
                        if sts:
                            time.sleep(.20)
                            sts = self.base.custObj.add_Seat(seatObj)
                        idx_seatObjList_AllSeatsNeeded += 1

                time.sleep(5)
                return sts
        except Exception as e:
            self.log.debug(f"\n{str(e)}")
        return sts


    def validate_AllSeatsNeeded_Found(self, custObj, seatObj):
        sts = True
        try:
            custObj.seatObjList_AllSeatsNeeded.clear()
            rowMax = self.getMax_SeatsInRowSection(seatObj)
            if(seatObj.seatIdx + custObj.seatsTotalNeeded) > rowMax:
                seatObj.dirLR = "R"
            tseatObj = copy.copy(seatObj)
            while (sts == True) and (len(custObj.seatObjList_AllSeatsNeeded) < custObj.seatsTotalNeeded):
                idxSeatType = 0
                # used to store the sel for a valid seat
                #sel = self.getSel_SpecificSeatOnMap(tseatObj)
                sel = self.getSel_SpecificSeat_FromAllSeatTypes_IfFound(custObj, tseatObj)
                if (sel is not None):
                    seatObjAdd = copy.copy(tseatObj)
                    custObj.seatObjList_AllSeatsNeeded.append(seatObjAdd)
                    custObj.increment_SeatsSelected_BySeatType(seatObjAdd)
                    if (len(custObj.seatObjList_AllSeatsNeeded) < custObj.seatsTotalNeeded):
                        # don't increment out-of-bounds
                        if(seatObj.dirLR == "L"):
                            if((tseatObj.seatIdx) < rowMax):
                                tseatObj.seatIdx += 1
                            else:
                                sts = False
                        else:
                            if ((tseatObj.seatIdx) > 1):
                                tseatObj.seatIdx -= 1
                            else:
                                sts = False

                        tseatObj.update_Info()
                        ele_Seat = self.getEle_SpecificSeatOnMap(tseatObj)
                        txt_Id = ele_Seat.get_attribute('id')
                        txt_SeatType = ele_Seat.get_attribute('class')
                        tseatObj.setup(txt_Id, txt_SeatType)
                else:
                    sts = False

            if (sts == True):
                rowMax = self.getMax_SeatsInRowSection(seatObj)
                # check for lone leafs
                if (seatObj.seatIdx == 1):
                    # first seat is at index 1
                    # only check left end
                    tseatObjL = copy.copy(tseatObj)
                    sts = self.check_LeftEnd(custObj, tseatObjL)
                elif (seatObj.seatIdx > 1) and (seatObj.seatIdx < rowMax):
                    # first seat is at between 1 and max seats in row
                    if seatObj.dirLR == "L":
                        # check dirLR == "L"
                        # check left and right ends
                        tseatObjL = copy.copy(tseatObj)
                        sts = self.check_LeftEnd(custObj, tseatObjL)
                        if sts:
                            tseatObjR = copy.copy(seatObj)
                            sts = self.check_RightEnd(custObj, tseatObjR)
                    else:
                        # check dirLR == "R"
                        # check left and right ends
                        tseatObjL = copy.copy(seatObj)
                        sts = self.check_LeftEnd(custObj, tseatObjL)
                        if sts:
                            tseatObjR = copy.copy(tseatObj)
                            sts = self.check_RightEnd(custObj, tseatObjR)
                elif (seatObj.seatIdx == rowMax):
                    # first seat is at max seats in row
                    # only check right end
                    tseatObjR = copy.copy(tseatObj)
                    sts = self.check_RightEnd(custObj, tseatObjR)

            return sts
        except Exception as e:
            self.log.debug(f"\n{str(e)}")


    def check_RightEnd(self, custObj, tseatObj):
        sts = True
        tseatObj.seatIdx -= 1
        tseatObj.update_Info()
        if (tseatObj.seatIdx >= 1):
            seatType1 = self.getSeatType_SpecificSeat_FromAllSeatTypes(custObj, tseatObj)
            if (seatType1 is not None):
                tseatObj.seatIdx -= 1
                tseatObj.update_Info()
                if (tseatObj.seatIdx >= 1):
                    seatType2 = self.getSeatType_SpecificSeat_FromAllSeatTypes(custObj, tseatObj)
                    if (seatType2 is not None):
                        if seatType1 == seatType2:
                            # indicated OK
                            pass
                        else:
                            # indicated a lone leaf
                            sts = False
                    else:
                        # indicated a lone leaf
                        sts = False
                else:
                    # indicated a lone leaf
                    sts = False
            else:
                # indicated OK
                pass
        return sts

    def check_LeftEnd(self, custObj, tseatObj):
        sts = True
        rowMax = self.getMax_SeatsInRowSection(tseatObj)
        tseatObj.seatIdx += 1
        tseatObj.update_Info()
        if (tseatObj.seatIdx <= rowMax):
            seatType1 = self.getSeatType_SpecificSeat_FromAllSeatTypes(custObj, tseatObj)
            if (seatType1 is not None):
                tseatObj.seatIdx += 1
                tseatObj.update_Info()
                if (tseatObj.seatIdx <= rowMax):
                    seatType2 = self.getSeatType_SpecificSeat_FromAllSeatTypes(custObj, tseatObj)
                    if (seatType2 is not None):
                        if seatType1 == seatType2:
                            # indicated OK
                            pass
                        else:
                            # indicated a lone leaf
                            sts = False
                    else:
                        # indicated a lone leaf
                        sts = False
                else:
                    # indicated a lone leaf
                    sts = False
            else:
                # indicated OK
                pass
        return sts
        return sts

    # used to store the sel for a valid seat
    def getSel_SpecificSeat_FromAllSeatTypes_IfFound(self, custObj, seatObj):
        # used to store the sel for a valid seat
        sel = None
        if (custObj.getNum_SeatsNeeded_BySeatType(seatObj.txt_SeatType) > 0):
            sel = self.getSel_SpecificSeatOnMap_bySeatType(seatObj)
        return sel

    # used to store the sel for a valid seat
    def getSeatType_SpecificSeat_FromAllSeatTypes(self, custObj, seatObj):
        # used to store the sel for a valid seat
        ret_SeatType = None
        idxSeatType = 0
        idxMax = len(custObj.listSelTxts_AllSeatTypes)
        while (ret_SeatType is None) and (idxSeatType < idxMax):
            txt_SeatType = custObj.listSelTxts_AllSeatTypes[idxSeatType]
            custObj.txt_SeatType = txt_SeatType
            seatObj.txt_SeatType = txt_SeatType
            seatObj.update_Info()
            sel = self.getSel_SpecificSeatOnMap_bySeatType(seatObj)
            if (sel is not None):
                ret_SeatType = txt_SeatType
                return ret_SeatType
            idxSeatType += 1
        return ret_SeatType


    def click_SectionAndSeatOnPage_ByIndex(self, sel, seatIdx, seatType):
        sts = False
        try:
            txt_Sel = f"( {sel[1]} ) [{seatIdx}]"
            sel_New = [sel[0], txt_Sel]

            element = self.driver.find_element(*sel_New)
            txt_Id = element.get_attribute('id')
            seatObj = SeatObj()
            seatObj.setup(txt_Id, seatType)

            seatCnt = self.getMax_SeatsInRowSection(seatObj)

            sts = self.click_Section_BySeatObj(seatObj)
            if sts:
                sts = self.click_Seat(seatObj)
                if sts:
                    sts = self.base.custObj.add_Seat(seatObj)

            return sts
        except Exception as e:
            self.log.debug(f"\n{str(e)}")


    def click_AddToCartButton_gotoPage__ADASeatingPopUp_WalmartAMP(self):
        self.base.goTo_PageBySel(self.sel_ButtonAddToCart, 5)
        page = ADASeatingPopUp_WalmartAMP(self.base)
        page.confirm_OnPage()
        return page


    def getExists_InvalidSession_PleaseRemoveTheHighlightedSeats(self):
        sts = self.base.confirm_ElementOnPage(self.sel_InvalidSession_PleaseRemoveTheHighlightedSeats)
        return sts


    def removeSeats_from_PreCart(self):
        eleList_X = []
        eleList_X = self.base.get_ElementsOnPage(self.sel_XButton_InPreCart)
        maxX = len(eleList_X)
        idxX = maxX - 1
        while (idxX >= 0):
            self.base.click_ElementOnPage(eleList_X[idxX])
            time.sleep(1)
            idxX -= 1


