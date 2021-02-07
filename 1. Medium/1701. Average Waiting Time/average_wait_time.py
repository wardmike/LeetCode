# Prompt: https://leetcode.com/problems/average-waiting-time/
# Runtime: 1348 ms, faster than 5.02% of Python online submissions for Average Waiting Time.
# Memory Usage: 58 MB, less than 78.14% of Python online submissions for Average Waiting Time.


class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        totalWait = 0.0 # cumulative wait of all customers (made a float for division at end)
        
        currentTime = 0
        
        for c in customers:
            arrivalTime = c[0]
            timeToCook = c[1]
            
            if arrivalTime > currentTime:
                currentTime = arrivalTime # cook waits between orders
            
            currentTime += timeToCook
            totalWait += (currentTime - arrivalTime)
            

        return totalWait / len(customers)
