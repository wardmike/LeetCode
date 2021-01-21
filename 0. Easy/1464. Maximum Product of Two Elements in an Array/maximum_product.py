# Prompt: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Runtime: 28 ms, faster than 98.32% of Python online submissions for Maximum Product of Two Elements in an Array.
# Memory Usage: 13.6 MB, less than 34.68% of Python online submissions for Maximum Product of Two Elements in an Array.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums, reverse=True)
        return (sortedNums[0] - 1) * (sortedNums[1] - 1)
