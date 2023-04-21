from selenium.webdriver.common.by import By
from utilities.BaseUtilities import BaseUtilities


class SelectedObj:

    # hash dict to hold artistNames and Cnt
    def __init__(self, sectionId, rowLetter, seatId):
        # et (element text) for selector
        self.seltxt_SeatsInSelected = "// div[contains( @class , 'flex items-center gap-4')] // div[contains( @ class, 'flex items-center gap-1')]"
        self.sectionIdxSM = sectionId
        self.rowLetter  = rowLetter
        self.seatIdx = seatId


    def get_SeatIdx(self):
        return self.seatIdx

    def get_RowLetter(self):
        return self.rowLetter

    def get_sectionIdxSM(self):
        return self.sectionIdxSM


