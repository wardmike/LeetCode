# Prompt: https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums):
        i = 0 #index as we go through nums
        last_added = -2 #start at -2 so nums[0] can be added
        arr = []
        #using a while so we can easily skip adjacent houses
        while i < len(nums) - 1: 
            try_val, compare_val = 0, 0
            for x in range(i,last_added+1,-2):
                try_val += nums[x]
            #check nums[i+1] to make sure we aren't missing out
            for x in range(i+1,last_added+1,-2):
                compare_val += nums[x]
            if try_val > compare_val:
                for x in range(i,last_added+1,-2):
                    arr.append(nums[x])
                last_added = i
                i = i + 2 #skip forward because nums[i+1] can't be added now
            else:
                i = i + 1
        #see if we can add the last one (and potentially more before it)
        if i == len(nums) - 1:
            for x in range(i,last_added+1,-2):
                arr.append(nums[x])
        return sum(arr)
