# Prompt: https://leetcode.com/problems/max-increase-to-keep-city-skyline
# Runtime: 48 ms, faster than 83.68% of Python3 online submissions for Max Increase to Keep City Skyline.
# Memory Usage: 13.2 MB, less than 5.55% of Python3 online submissions for Max Increase to Keep City Skyline.

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skylineTop = len(grid[0]) * [0] # skyline as viewed from the top
        skylineSide = len(grid) * [0] # skyline as viewed from the side
        
        totalCanAdd = 0
        
        # find skyline vals
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                val = grid[y][x]
                if val > skylineTop[x]:
                    skylineTop[x] = val
                if val > skylineSide[y]:
                    skylineSide[y] = val
                    
        # check each building height; if it's less than min of skyline viewed in both directions, height can be increased
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                val = grid[y][x]
                maxHeight = min(skylineTop[x], skylineSide[y]) # max height without affecting skyline
                totalCanAdd += maxHeight - val # diff can't be negative here
        return totalCanAdd
