import time

from selenium.webdriver.common.by import By

from sites.WalmartAMP.objects.ProductionObj import ProductionObj
from sites.WalmartAMP.pages.PerformanceDetails_WalmartAMP import PerformanceDetails_WalmartAMP


class Calendar_WalmartAMP:
    # define selectors elements
    sel_ConfirmPage = (By.XPATH, "(//div[contains(string(),'Calendar')]) [1]")
    sel_ArtistName = (By.XPATH, "//div[contains(@class, 'text-2xl font-bold lg:text-3xl')]")
    sel_ArtistPic = (By.XPATH, "//img[contains(@srcset, '/_next/image')]")

    # hash dict to hold artistNames and ProductionObjs
    dict_ArtistName_ProductionObj = {}
    list_IdxList_ArtistName = []

    def __init__(self, base):
        self.base = base
        self.driver = base.getDriver()
        self.dictArtistMax = 0
        self.listArtistMax = 0

    def confirm_OnPage(self):
        self.base.confirm_OnPage(self.sel_ConfirmPage, 10)
        self.initDataForAllArtist()


    def initDataForAllArtist(self):
        eleList_ArtistName = self.driver.find_elements(*self.sel_ArtistName)
        self.list_IdxList_ArtistName = []
        self.dict_ArtistName_ProductionObj = {}
        # create list of eArtists
        if len(eleList_ArtistName) > 0:
            idxList = 0
            for eArtist in eleList_ArtistName:
                # set idxArtist
                idxArtist = idxList + 1
                artistName = eArtist.text

                # insert in list_IdxList_ArtistName
                self.list_IdxList_ArtistName.insert(idxList, artistName)

                # insert or update in dict_ArtistName_ProductionObj
                if artistName not in self.dict_ArtistName_ProductionObj:
                    #create new ProductionObj
                    productionObj = ProductionObj(artistName)
                    productionObj.add_PerfIdx(idxArtist)
                    self.dict_ArtistName_ProductionObj[artistName] = productionObj
                else:
                    # update existing ProductionObj
                    productionObj = self.dict_ArtistName_ProductionObj[artistName]
                    productionObj.add_PerfIdx(idxArtist)
                    self.dict_ArtistName_ProductionObj[artistName] = productionObj

                # increment idxList
                idxList = idxList + 1

            self.dictArtistMax = len(self.dict_ArtistName_ProductionObj)
            self.listArtistMax = len(self.list_IdxList_ArtistName)

    def getDictArtistMax(self):
        return self.dictArtistMax

    def get_ProductionMax(self):
        return self.listArtistMax


    def getProductionObj_ByNumberOfPerfs(self, numOfPerfs, perfIdx):
        # select first eArtist with only a single production
        productionObj = None
        idxList = perfIdx - 1
        while(idxList < self.listArtistMax):
            artistName = self.list_IdxList_ArtistName[idxList]
            if artistName in self.dict_ArtistName_ProductionObj:
                productionObj = self.dict_ArtistName_ProductionObj[artistName]
                if productionObj.perfCnt == numOfPerfs:
                    return productionObj
            idxList = idxList + 1
        return productionObj


    def clickArtistPic_gotoPage_PerformanceDetails_WalmartAMP(self, perfIdx, artistName):
        self.base.goTo_PageByClickingElementInList(self.sel_ArtistPic, perfIdx, 5)
        page = PerformanceDetails_WalmartAMP(self.base, artistName)
        page.confirm_OnPage()
        return page
