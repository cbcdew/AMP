from selenium.webdriver.common.by import By


class SeatObj:

    txt_SeatType_Available = 'available'
    txt_SeatType_Regular = 'regular_seat'
    txt_SeatType_Regular_Available = 'regular_seat available'
    txt_SeatType_Companion = 'accessible_companion_seat'
    txt_SeatType_Companion_Available = 'accessible_companion_seat available'
    txt_SeatType_Wheelchair = 'accessible_wheelchair_seat'
    txt_SeatType_Wheelchair_Available = 'accessible_wheelchair_seat available'

    sel_Seat_Available = [By.XPATH, "//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@class, ' available')]"]
    sel_Seat_Regular_Available = [By.XPATH, "//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'g') and contains(@id, 'R-007')]  //*[contains(name(),'circle') and contains(@class, ' available')]"]
    sel_Seat_Companion_Available = [By.XPATH, "//*[local-name()='circle' and @class='accessible_companion_seat available']"]
    sel_Seat_Wheelchair_Available = [By.XPATH, "//*[local-name()='circle' and @class='accessible_wheelchair_seat available']"]

    # new seats in row...
    # //div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'g') and contains(@id, 'R-007')]  //*[contains(name(),'circle') and contains(@class, ' available')]

    xsel_Seat_Available = [By.XPATH, "//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@class, ' available')]"]
    xsel_Seat_Regular_Available = [By.XPATH, "//div[contains(@class, 'react-transform-component')] //*[local-name()='circle' and @class='regular_seat available']"]
    xsel_Seat_Companion_Available = [By.XPATH, "//div[contains(@class, 'react-transform-component')] //*[local-name()='circle' and @class='accessible_companion_seat available']"]
    xsel_Seat_Wheelchair_Available = [By.XPATH, "//div[contains(@class, 'react-transform-component')] //*[local-name()='circle' and @class='accessible_wheelchair_seat available']"]

    # //div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@class, 'accessible_wheelchair_seat available')]
    # // div[contains( @class , 'flex items-center gap-4')] // div[contains( @ class, 'flex items-center gap-1')]



    def __init__(self):
        self.seatIdx = 1
        self.rowLetter = "S"
        self.sectionIdxSM = 8
        self.sectionIdxLG = 166
        self.txt_SeatType = ""
        self.sel_SeatType = None
        self.txt_Id = ""
        self.dirLR = "L"

        # hash dict to hold artistNames and Cnt
        #id="seat-19-R-8-166"
        #working:    //div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, 'seat-18-R-8-166') and contains(@class, 'accessible_companion_seat available')]
        self.seltxt_SeatsInSection_Available = ""
        self.seltxt_SeatsInRow = ""
        self.seltxt_SeatsInRow_ByType = ""
        self.seltxt_SpecificSeatOnMap = ""
        self.seltxt_SpecificSeatOnMap_bySeatType = ""
        self.seltxt_SeatInSelected = ""


    def setup(self, txt_Id, txt_SeatType):
        list_SeatParts = txt_Id.split('-')
        self.seatIdx = int(list_SeatParts[1])
        self.rowLetter = list_SeatParts[2]
        self.sectionIdxSM = int(list_SeatParts[3])
        self.sectionIdxLG = int(list_SeatParts[4])
        self.txt_SeatType = txt_SeatType
        self.sel_SeatType = None
        self.set_selSeatType_By_txtSeatType(txt_SeatType)
        self.update_Info()


    def get_Id(self):
        return self.txt_Id

    def get_SeatIdx(self):
        return self.seatIdx

    def set_selSeatType_By_txtSeatType(self, txt_SeatType):
        if txt_SeatType == self.txt_SeatType_Wheelchair_Available:
            self.sel_SeatType = self.sel_Seat_Wheelchair_Available
        elif txt_SeatType == self.txt_SeatType_Companion_Available:
            self.sel_SeatType = self.sel_Seat_Companion_Available
        elif txt_SeatType == self.txt_SeatType_Regular_Available:
            self.sel_SeatType = self.sel_Seat_Regular_Available

    def update_Info(self):
        self.txt_Id = f"seat-{self.seatIdx}-{self.rowLetter}-{self.sectionIdxSM}-{self.sectionIdxLG}"

        self.seltxt_SeatsInSection_Available = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.sectionIdxSM}-{self.sectionIdxLG}') and contains(@class, ' available')]"
        self.seltxt_SeatsInRow = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.rowLetter}-{self.sectionIdxSM}-{self.sectionIdxLG}')]"
        self.seltxt_SeatsInRow_Available = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.rowLetter}-{self.sectionIdxSM}-{self.sectionIdxLG}') and contains(@class, ' available')]"
        self.seltxt_SeatsInRow_Regular_Available = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.rowLetter}-{self.sectionIdxSM}-{self.sectionIdxLG}') and contains(@class, 'regular_seat available')]"
        self.seltxt_SeatsInRow_Wheelchair_Available = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.rowLetter}-{self.sectionIdxSM}-{self.sectionIdxLG}') and contains(@class, 'accessible_wheelchair_seat available')]"
        self.seltxt_SeatsInRow_Companion_Available = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.rowLetter}-{self.sectionIdxSM}-{self.sectionIdxLG}') and contains(@class, 'accessible_companion_seat available')]"

        self.seltxt_SeatsInRow_ByType = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.rowLetter}-{self.sectionIdxSM}-{self.sectionIdxLG}') and contains(@class, '{self.txt_SeatType}')]"
        self.seltxt_SpecificSeatOnMap = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.txt_Id}')]"
        self.seltxt_SpecificSeatOnMap_bySeatType = f"//div[contains(@class, 'react-transform-component')] //*[contains(name(),'svg')] //*[contains(name(),'circle') and contains(@id, '{self.txt_Id}') and contains(@class, '{self.txt_SeatType}')]"
        self.seltxt_SeatInSelected = f"// div[contains( @class , 'flex items-center gap-4')] // div[contains( @ class, 'flex items-center gap-1')]"



    def get_RowLetter(self):
        return self.rowLetter

    def get_sectionIdxSM(self):
        return self.sectionIdxSM

    def get_sectionIdxLG(self):
        return self.sectionIdxLG

