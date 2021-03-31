# Prompt: https://leetcode.com/problems/design-underground-system/
# Runtime: 232 ms, faster than 64.15% of Python online submissions for Design Underground System.
# Memory Usage: 24.8 MB, less than 80.18% of Python online submissions for Design Underground System.


class UndergroundSystem(object):

    def __init__(self):
        self.times = {} # maps routeId to times
        
        self.currentCheckinTimes = {} # maps customer id to checkin time
        
        self.currentCheckinStations = {} # maps customer id to checkin station
        
    def __getRouteId(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: str
        """
        return startStation + "_" + endStation
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.currentCheckinTimes[id] = t
        self.currentCheckinStations[id] = stationName
        
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        checkinTime = self.currentCheckinTimes[id]
        checkinStation = self.currentCheckinStations[id]
        
        route = self.__getRouteId(checkinStation, stationName)
        
        if route in self.times:
            self.times[route].append(t - checkinTime)
        else:
            self.times[route] = [t - checkinTime]
            
        del self.currentCheckinTimes[id]
        del self.currentCheckinStations[id]
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        route = self.__getRouteId(startStation, endStation)
        return sum(self.times[route]) / float(len(self.times[route]))
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
