# Prompt: https://leetcode.com/problems/two-sum
# Runtime: 5368 ms, faster than 15.64% of Python3 online submissions for Two Sum.
# Memory Usage: 13.7 MB, less than 39.38% of Python3 online submissions for Two Sum.
# efficiency is O(n^2); using a tree might be able to get it to O(log(n))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
