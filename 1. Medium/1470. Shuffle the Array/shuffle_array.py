# Prompt: https://leetcode.com/problems/shuffle-the-array/
# Runtime: 48 ms, faster than 47.26% of Python online submissions for Shuffle the Array.
# Memory Usage: 13.7 MB, less than 43.14% of Python online submissions for Shuffle the Array.


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = []
        y = []
        
        for i in range(n):
            x.append(nums[i])
            y.append(nums[n+i])
            
        final = []
        
        for i in range(n):
            final.append(x[i])
            final.append(y[i])
            
        return final
