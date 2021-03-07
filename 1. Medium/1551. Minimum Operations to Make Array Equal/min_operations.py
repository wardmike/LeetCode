# Prompt: https://leetcode.com/problems/minimum-operations-to-make-array-equal/
# Runtime: 160 ms, faster than 13.67% of Python online submissions for Minimum Operations to Make Array Equal.
# Memory Usage: 14.1 MB, less than 5.04% of Python online submissions for Minimum Operations to Make Array Equal.


class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        nums = []
        for i in range(n):
            nums.append(1 + (i * 2))
            
        goal = sum(nums) / n
            
        operations = 0        
    
        # only need to count operations of numbers less than goal
        # because numbers above goal are mirrored by those operations
        for num in nums:
            if num <= goal:
                operations += (goal - num)
                
        return operations
