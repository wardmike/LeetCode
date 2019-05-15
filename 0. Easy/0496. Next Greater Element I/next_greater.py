# Prompt: https://leetcode.com/problems/next-greater-element-i

# Runtime: 60 ms, faster than 37.16% of Python online submissions for Next Greater Element I.
# Memory Usage: 12 MB, less than 48.05% of Python online submissions for Next Greater Element I.

class Solution(object):
    # finds the next greater number after index in arr
    def nextGreater(self, arr, index):
        for i in range(index+1, len(arr)):
            if arr[i] > arr[index]:
                return arr[i]
        return -1
        
    def nextGreaterElement(self, nums1, nums2):
        # pre-compute next greater for each num in num2 (saves time later)
        nextGreater = {} # we can use a hash map because numbers are unique
        for index, num  in enumerate(nums2):
            nextGreater[num] = self.nextGreater(nums2, index)
        # go through each num in nums1 & look up next greater number
        result = []
        for num in nums1:
            result.append(nextGreater[num])
            
        return result
