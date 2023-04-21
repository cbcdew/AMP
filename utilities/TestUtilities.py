import time

from sites.WalmartAMP.components.HeaderMenu_WalmartAMP import HeaderMenu_WalmartAMP
from sites.WalmartAMP.pages.Home_WalmartAMP import Home_WalmartAMP
from utilities.BaseUtilities import BaseUtilities


class TestUtilities:
    
    def __init__(self, driver):
        self.driver = driver
        self.base = BaseUtilities(driver)


    def init_GoTo_SeatMap(self, custObj):
        home = Home_WalmartAMP(self.base)
        home.goto_HomePageURL()
        headerMenu = HeaderMenu_WalmartAMP(self.base)
        seatMap = None

        productionIdx = 1
        perfIdx = 1
        # goto Calendar page
        calendar = headerMenu.click_ele_Calendar()
        perfIdx = 0
        productionMax = calendar.get_ProductionMax()
        sts = False
        while (sts == False) and (productionIdx <= productionMax):
            productionObj = calendar.getProductionObj_ByNumberOfPerfs(custObj.numOfPerfs, productionIdx)
            if (productionObj != None):
                # get artist name
                artistName = productionObj.artistName
                # get perfIdx
                perfIdx = productionObj.get_PerfIdx(1)
                performanceDetails = calendar.clickArtistPic_gotoPage_PerformanceDetails_WalmartAMP(perfIdx, artistName)
                time.sleep(2)
                seatMap = performanceDetails.clickBuyTicketsButton_gotoPage_SeatMap_WalmartAMP(artistName)
                custObj.txt_ArtistName = artistName
                if seatMap.process_Validate_SeatsAvailable(custObj):
                    sts = True
                else:
                    calendar = None
                    seatMap = None
                    performanceDetails = None
                    calendar = headerMenu.click_ele_Calendar()
                    productionMax = calendar.get_ProductionMax()
            # take the last known perfIdx and ad 1 - skips to next artist with single perf.
            productionIdx = perfIdx + 1

        return seatMap