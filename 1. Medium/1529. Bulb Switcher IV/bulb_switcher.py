# Prompt: https://leetcode.com/problems/bulb-switcher-iv/
# Runtime: 84 ms, faster than 53.85% of Python online submissions for Bulb Switcher IV.
# Memory Usage: 14.5 MB, less than 86.81% of Python online submissions for Bulb Switcher IV.

class Solution(object):
    
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        # count groupings of 0s and 1s starting with the first 1
        # that will give number of flips
        
        inBeginning = True # before first 1 is reached
        prevBulb = "1"
        flips = 0
        for bulb in target:
            if inBeginning:
                if bulb == "1": # reached first 1
                    inBeginning = False
                    flips += 1
            else:
                if bulb != prevBulb: # new grouping
                    prevBulb = bulb
                    flips += 1
        
        return flips
