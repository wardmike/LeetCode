# Prompt: https://leetcode.com/problems/number-of-1-bits
# Runtime: 24 ms, faster than 58.04% of Python online submissions for Number of 1 Bits.
# Memory Usage: 11.6 MB, less than 5.10% of Python online submissions for Number of 1 Bits.

class Solution(object):
    def hammingWeight(self, n):
        oneBitCount = 0
        while n: # is "False" if it has no 1s
            oneBitCount += (1 & n)
            n >>= 1
        return oneBitCount
        
        
        
