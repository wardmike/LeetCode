# Prompt: https://leetcode.com/problems/array-partition-i/submissions/
"""
 notes: maybe sort it and then pick pairs?
 biggest will be lost no matter what; how can we make sure we get the 2nd biggest?
 could probably save memory if we sorted in place
"""
# Runtime: 100 ms, faster than 73.23% of Python3 online submissions for Array Partition I.
# Memory Usage: 15 MB, less than 5.20% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort and then pick every two (smallest from each pair); this ensures that
        # mins are as big as possible
        sortedNums = sorted(nums)
        total = 0 # sum of mins
        for i in range(0, len(sortedNums), 2):
            total += sortedNums[i]
        return total
