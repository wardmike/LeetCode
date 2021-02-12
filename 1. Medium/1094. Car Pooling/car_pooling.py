# Prompt: https://leetcode.com/problems/car-pooling/
# Runtime: 84 ms, faster than 25.22% of Python online submissions for Car Pooling.
# Memory Usage: 13.9 MB, less than 68.47% of Python online submissions for Car Pooling.


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        inCar = 0
        currentPos = 0
        
        # maps drop-off location to num passengers to drop off there
        dropOff = {}
        
        # sort by pick-up location
        sortedTrips = sorted(trips, key=lambda trip: trip[1])

        for t in sortedTrips:
            # parse trip
            numPass = t[0]
            start = t[1]
            end = t[2]
            
            # check if trip pick-up is west of current pos
            if start < currentPos:
                print("start")
                return False
            
            # drop off passengers
            toDel = []
            for key in dropOff:
                if key <= start:
                    inCar -= dropOff[key]
                    toDel.append(key)
            # delete entries for dropped-off passengers
            for k in toDel:
                del dropOff[k]
            
            # pick up passengers & update position
            inCar += numPass
            currentPos = start
            if inCar > capacity:
                return False
        
            # schedule drop-off
            if end in dropOff:
                dropOff[end] += numPass
            else:
                dropOff[end] = numPass
        
        return True
