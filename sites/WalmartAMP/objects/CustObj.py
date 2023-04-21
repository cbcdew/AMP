from sites.WalmartAMP.objects.SeatObj import SeatObj


class CustObj:

    # hash dict to hold artistNames and Cnt


    def __init__(self):
        self.txt_ArtistName = ""
        self.txt_CustName = ""
        self.txt_CC = ""
        self.txt_CVV = ""
        self.txt_Month = ""
        self.txt_Year = ""

        self.txt_FirstName = ""
        self.txt_LastName = ""
        self.txt_Email = ""
        self.txt_Password = ""
        self.txt_PhoneNumber = ""
        self.txt_Addr1 = ""
        self.txt_Addr2 = ""
        self.txt_City = ""
        self.seltxt_State = None
        self.txt_State = ""
        self.txt_Zip = ""

        self.numOfPerfs = 0
        self.seatCnt = 0
        self.seatsTotalNeeded = 0
        self.sel_SeatType = None
        self.txt_SeatType = ""
        self.seatsToBuy_Regular = 0
        self.seatsSelected_Regular = 0
        self.seatsToBuy_WheelChair = 0
        self.seatsSelected_WheelChair = 0
        self.seatsToBuy_Companion = 0
        self.seatsSelected_Companion = 0
        self.seatObjList_AllSeatsNeeded = []

        self.dict_seatCnt_SeatObj = {}
        self.listSels_AllSeatTypes = []
        self.listSelTxts_AllSeatTypes = []


    def add_Seat(self, seatObj):
        sts = False
        self.seatCnt = self.seatCnt + 1
        if self.seatCnt not in self.dict_seatCnt_SeatObj:
            self.dict_seatCnt_SeatObj[self.seatCnt] = seatObj
            sts = True
        return sts


    def get_SeatsTotalNeeded(self):
        self.seatsTotalNeeded += self.seatsToBuy_Regular
        self.seatsTotalNeeded += self.seatsToBuy_WheelChair
        self.seatsTotalNeeded += self.seatsToBuy_Companion
        return self.seatsTotalNeeded


    def get_LastSeatAdded(self):
        seatObj = None
        if self.seatCnt in self.dict_seatCnt_SeatObj:
            seatObj = self.dict_seatCnt_SeatObj[self.seatCnt]
        return seatObj


    def get_Seat(self, seatIdx):
        seatObj = None
        if seatIdx in self.dict_seatCnt_SeatObj:
            seatObj = self.dict_seatCnt_SeatObj[seatIdx]
        return seatObj


    def getNum_SeatsNeeded_BySeatType(self, txt_SeatType):
        cnt = 0
        if txt_SeatType == SeatObj.txt_SeatType_Regular_Available:
            cnt = self.seatsToBuy_Regular - self.seatsSelected_Regular
        elif txt_SeatType == SeatObj.txt_SeatType_Wheelchair_Available:
            cnt = self.seatsToBuy_WheelChair - self.seatsSelected_WheelChair
        elif txt_SeatType == SeatObj.txt_SeatType_Companion_Available:
            cnt = self.seatsToBuy_Companion - self.seatsSelected_Companion
        return cnt


    def resetSelected(self):
        self.seatsSelected_Regular = 0
        self.seatsSelected_WheelChair = 0
        self.seatsSelected_Companion = 0


    def increment_SeatsSelected_BySeatType(self, seatObj):
        sts = False
        if seatObj.txt_SeatType == SeatObj.txt_SeatType_Regular_Available:
            self.seatsSelected_Regular += 1
            sts = True
        elif seatObj.txt_SeatType == SeatObj.txt_SeatType_Wheelchair_Available:
            self.seatsSelected_WheelChair += 1
            sts = True
        elif seatObj.txt_SeatType == SeatObj.txt_SeatType_Companion_Available:
            self.seatsSelected_Companion += 1
            sts = True
        return sts


    def createList_AllSeatTypes(self):
            self.listSels_AllSeatTypes.append(SeatObj.sel_Seat_Wheelchair_Available)
            self.listSelTxts_AllSeatTypes.append(SeatObj.txt_SeatType_Wheelchair_Available)
            self.listSels_AllSeatTypes.append(SeatObj.sel_Seat_Companion_Available)
            self.listSelTxts_AllSeatTypes.append(SeatObj.txt_SeatType_Companion_Available)
            self.listSels_AllSeatTypes.append(SeatObj.sel_Seat_Regular_Available)
            self.listSelTxts_AllSeatTypes.append(SeatObj.txt_SeatType_Regular_Available)

