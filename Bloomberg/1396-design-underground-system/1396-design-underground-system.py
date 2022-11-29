class UndergroundSystem:

    def __init__(self):
        # checkInDict {id: (startStation, checkInTime)}
        # tripDict {(startStation, endStation): [totalTime += checkOutTime - checkIntime, count]}
        self.checkInDict = {}
        self.tripDict = {}
                       

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInDict[id] = (stationName, t)
        return
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkInTime = self.checkInDict[id]
        # del self.checkInDict[id]
        if (startStation, stationName) not in self.tripDict:
            self.tripDict[(startStation, stationName)] = [t - checkInTime, 1]
        else:
            self.tripDict[(startStation, stationName)][0] += (t - checkInTime)
            self.tripDict[(startStation, stationName)][1] += 1
        return
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.tripDict:
            return
        else:
            
            totalTime = self.tripDict[(startStation, endStation)][0]
            count = self.tripDict[(startStation, endStation)][1]
            return totalTime/count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)