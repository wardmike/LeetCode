# Prompt: https://leetcode.com/problems/maximum-subarray/
class Solution:
    """ This is a brute force O(n^2) solution. Memoizing may
    be able to make it faster. The prompt also mentions an O(n)
    solution and recommends the "divice and conquer approach."
    """
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        max_sub = nums[0]
        for i in range(0, len(nums)):
            temp_sub = 0
            for k in range(i, len(nums)):
                temp_sub += nums[k]
                if temp_sub > max_sub:
                    max_sub = temp_sub
        return max_sub
