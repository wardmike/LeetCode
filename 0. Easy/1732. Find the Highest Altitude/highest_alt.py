# Prompt: https://leetcode.com/problems/find-the-highest-altitude/
# Runtime: 24 ms, faster than 55.66% of Python online submissions for Find the Highest Altitude.
# Memory Usage: 13.2 MB, less than 94.80% of Python online submissions for Find the Highest Altitude.


class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        maxAlt = 0
        alt = 0
        
        for g in gain:
            alt += g
            if alt > maxAlt:
                maxAlt = alt
        
        
        return maxAlt
