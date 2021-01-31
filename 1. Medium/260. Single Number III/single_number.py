# Prompt: https://leetcode.com/problems/single-number-iii/
# Runtime: 44 ms, faster than 69.79% of Python online submissions for Single Number III.
# Memory Usage: 15.1 MB, less than 59.38% of Python online submissions for Single Number III.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numSet = set()
        
        for num in nums:
            if num not in numSet:
                # add every new number to set
                numSet.add(num)
            else:
                # if it's already in the set, remove it
                numSet.remove(num)
        
        # all numbers that were in the list twice will have
        # been added to the set and then removed; the only
        # numbers remaining in the set are the ones that
        # were only in the list once
                
        return list(numSet)
