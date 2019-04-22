# Prompt: https://leetcode.com/problems/trapping-rain-water
# Runtime: 48 ms, faster than 73.12% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 13.8 MB, less than 5.11% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        lenHeights = len(height)
        leftMax = [] # this is the max water that can accumulate if ONLY bounded on left side
        localMax = 0
        for l in height:
            if l > localMax:
                localMax = l
            leftMax.append(localMax)
        rightMax = [] # accumulation if ONLY bounded on right side
        localMax = 0
        for r in range(lenHeights-1, -1, -1):
            if height[r] > localMax:
                localMax = height[r]
            rightMax.append(localMax)
        water = 0
        # find the lower of the left & right bounds here; this is how high water can actually go
        for i in range(lenHeights):
            leftMaxHere = leftMax[i]
            rightMaxHere = rightMax[lenHeights-i-1] # rightMax arr is done in reverse
            maxHere = leftMaxHere if leftMaxHere < rightMaxHere else rightMaxHere
            water += max(maxHere - height[i], 0) # can't be negative water accumulation
        return water
        
