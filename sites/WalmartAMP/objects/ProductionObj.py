class ProductionObj:

    # hash dict to hold artistNames and Cnt

    def __init__(self, artistName):
        self.artistName = artistName
        self.perfCnt = 0
        self.dict_PerfCnt_ArtistIdxs = {}


    def add_PerfIdx(self, idxArtist):
        self.perfCnt = self.perfCnt + 1
        if self.perfCnt not in self.dict_PerfCnt_ArtistIdxs:
            self.dict_PerfCnt_ArtistIdxs[self.perfCnt] = idxArtist


    def get_PerfIdx(self, idxPerf):
        idxArtist = -1
        if idxPerf in self.dict_PerfCnt_ArtistIdxs:
            idxArtist = self.dict_PerfCnt_ArtistIdxs[idxPerf]
        return idxArtist
