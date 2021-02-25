# Prompt: https://leetcode.com/problems/arithmetic-subarrays/
# Runtime: 176 ms, faster than 71.32% of Python online submissions for Arithmetic Subarrays.
# Memory Usage: 13.7 MB, less than 34.11% of Python online submissions for Arithmetic Subarrays.


class Solution(object):
    
    def isArithmeticSequence(self, seq):
        if len(seq) < 2:
            return True
        diff = seq[1] - seq[0]
        
        for i in range(len(seq)-1):
            if seq[i+1] - seq[i] != diff:
                return False
        
        return True
    
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        
        output = []
        for i in range(len(l)):
            start = l[i]
            end = r[i]+1
            seq = sorted(nums[start:end])
            output.append(self.isArithmeticSequence(seq))
        
        return output
