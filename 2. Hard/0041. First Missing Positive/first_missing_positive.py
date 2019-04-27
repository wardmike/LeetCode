# Prompt: https://leetcode.com/problems/first-missing-positive
# Runtime: 36 ms, faster than 99.44% of Python3 online submissions for First Missing Positive.
# Memory Usage: 13.2 MB, less than 5.26% of Python3 online submissions for First Missing Positive.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        smallest = 1
        for num in nums:
            if num > smallest:
                return smallest
            elif num == smallest:
                smallest += 1
        return smallest
