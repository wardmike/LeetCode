# Prompt: https://leetcode.com/problems/sum-of-unique-elements/
# Runtime: 20 ms, faster than 83.82% of Python online submissions for Sum of Unique Elements.
# Memory Usage: 13.3 MB, less than 93.80% of Python online submissions for Sum of Unique Elements.


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        prevNum = 0
        unique = []
        first = False
        for num in nums:
            if num == prevNum:
                first = False
            else:
                if first:
                    unique.append(prevNum)
                prevNum = num
                first = True
                
        # add last number
        if first:
            unique.append(prevNum)
        
        return sum(unique)
