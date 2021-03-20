# Prompt: https://leetcode.com/problems/sort-colors/
# Runtime: 24 ms, faster than 48.61% of Python online submissions for Sort Colors.
# Memory Usage: 13.5 MB, less than 42.22% of Python online submissions for Sort Colors.


class Solution(object):
    
    def swap(self, arr, i, j):
        """
        :type arr: List[int]
        :type i: int
        :type j: int
        :rtype: None Do not return anything; modify arr in-place instead.
        """
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
    
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything; modify nums in-place instead.
        """
        
        # bubble sort
        allSorted = False
        
        while not allSorted:
            allSorted = True
            
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    self.swap(nums, i, i+1)
                    allSorted = False
                    
        return nums
