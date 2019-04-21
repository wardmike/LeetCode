# https://leetcode.com/problems/trapping-rain-water
# TIME LIMIT EXCEEDED
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        # iterate through from left to right
        # record the walls that might trap water on the left side
        # dict key will be altitude of the wall (each altitude must be added separately, as
        # water is only trapped at some altitudes, depending on if there is a wall on the right)
        # 1, 0, 1
        left_wall = {}
        prev = 0 # height of previous position visisted
        for h_i in range(len(height)): # h_i = 0
            h = height[h_i] # h = 1
            diff = h - prev # calculate height change # diff = 1
            if diff > 0: # going up
                for i in range(prev+1, h+1): # try all altitudes # range: 1
                    if i in left_wall:
                        water += h_i - left_wall[i] - 1
                    else:
                        left_wall[i] = h_i
            elif diff < 0: # going down
                for i in range(h, prev+1):
                    left_wall[i] = h_i - 1
            prev = h # update prev
        return water
