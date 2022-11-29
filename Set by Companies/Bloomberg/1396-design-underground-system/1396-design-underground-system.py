class UndergroundSystem:

    def __init__(self):
        """
        thoughts:
        when i see one place at a time, that reminds me of dict
        I will at least use one dict to reocrd id and check in time
        With checkout function we need to know its checkin and checkout time
        To calculate average, we need a total time and total count
        I can definitely put this data behind ids
        But I would have to go through all id and their start,end station 
        and find total time. This is tedious
        So lets use anoter dict, but the key should be something else
        We can use start station........
        No lets use tuple of (startStation, endStation) as key 
        and value to be [totalTime, count]
        """
        self.checkInDict = {} # {id: []startStation, checkInTime]}
        self.tripDict = {} # {(startStation, endStation): [totalTime, count]}
                            # totalTime = checkOutTime - checkInTime

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInDict[id] = (stationName, t)
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkInTime = self.checkInDict[id]
        if (startStation, stationName) not in self.tripDict:
            self.tripDict[(startStation, stationName)] = [t - checkInTime, 1]
        else:
            self.tripDict[(startStation, stationName)][0] += t - checkInTime
            self.tripDict[(startStation, stationName)][1] += 1
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.tripDict:
            return
        else:
            totalTime, count = self.tripDict[(startStation, endStation)]
            return totalTime / count
    
    """
    Time O(1) for all methods | Space O(P + S^2)
    P as total number of distinct passengers
    S as total number of stations, worse case is for each station pair
    there is one log.
    """


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)