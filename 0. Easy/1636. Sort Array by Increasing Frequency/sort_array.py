# Prompt: https://leetcode.com/problems/sort-array-by-increasing-frequency/
# Runtime: 164 ms, faster than 6.07% of Python online submissions for Sort Array by Increasing Frequency.
# Memory Usage: 13.4 MB, less than 82.50% of Python online submissions for Sort Array by Increasing Frequency.


class Solution(object):
    
    def swap(self, arr, i, j):
        """
        :type arr: List[int]
        :type i: int
        :type j: int
        :rtype: None
        """
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {} # maps num to frequency
        
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
    
        # simple bubble sort
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums)-1):
                if freq[nums[i]] == freq[nums[i+1]]:
                    if nums[i] < nums[i+1]:
                        self.swap(nums, i, i+1)
                        swapped = True
                elif freq[nums[i]] > freq[nums[i+1]]:
                    self.swap(nums, i, i+1)
                    swapped = True
        
        return nums
