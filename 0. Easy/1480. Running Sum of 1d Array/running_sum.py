# Prompt: https://leetcode.com/problems/running-sum-of-1d-array/
# Runtime: 24 ms, faster than 79.46% of Python online submissions for Running Sum of 1d Array.
# Memory Usage: 13.5 MB, less than 68.68% of Python online submissions for Running Sum of 1d Array.
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = 0
        sums = []
        for num in nums:
            running_sum += num
            sums.append(running_sum)
        return sums
