# Prompt: https://leetcode.com/problems/minimum-size-subarray-sum/
# Runtime: 3516 ms, faster than 5.01% of Python online submissions for Minimum Size Subarray Sum.
# Memory Usage: 15.6 MB, less than 24.22% of Python online submissions for Minimum Size Subarray Sum.


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minSoFar = 0
        currentBatch = []
        
        for n in nums:
            currentBatch.append(n)
            
            
            if sum(currentBatch) >= target:
                while sum(currentBatch[1:]) >= target:
                    currentBatch.pop(0)

                if len(currentBatch) < minSoFar or minSoFar is 0:
                    minSoFar = len(currentBatch)
        
        return minSoFar
