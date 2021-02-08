# Prompt: https://leetcode.com/problems/water-bottles/
# Runtime: 20 ms, faster than 48.33% of Python online submissions for Water Bottles.
# Memory Usage: 13.3 MB, less than 72.92% of Python online submissions for Water Bottles.


class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
        numFull = numBottles
        numEmpty = 0
        drank = 0
        
        while numFull > 0:
            # drink full waterbottles
            drank += numFull
            numEmpty += numFull
            # refill
            numFull = numEmpty // numExchange
            numEmpty = numEmpty % numExchange
            
        return drank
