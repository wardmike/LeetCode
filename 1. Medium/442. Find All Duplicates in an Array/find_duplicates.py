# Prompt: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Runtime: 300 ms, faster than 87.30% of Python online submissions for Find All Duplicates in an Array.
# Memory Usage: 22.8 MB, less than 25.22% of Python online submissions for Find All Duplicates in an Array.


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        once = set()
        
        twice = set()
        
        for num in nums:
            if num in once:
                twice.add(num)
            else:
                once.add(num)
                
        return list(twice)
