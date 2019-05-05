# Prompt: https://leetcode.com/problems/counting-bits
"""
 Notes: start at 0 and keep incrementing the binary number until it gets to the input
 "num". The idea here is that each time the binary number increases in length, the entire current 
 series is repeated with an extra "1" at the beginning.
"""
# Runtime: 88 ms, faster than 73.98% of Python online submissions for Counting Bits.
# Memory Usage: 15.7 MB, less than 7.94% of Python online submissions for Counting Bits.

import copy

class Solution(object):
    def countBits(self, num):
        result = [0]
        subIndex = 0
        subLen = 1 
        nextPowTwo = 1
        for i in range(1, num+1):
            result.append(result[subIndex]+1) # +1 for the extra 1 at the beginning
            subIndex += 1
            if subIndex == subLen:
                subLen = len(result)
                subIndex = 0
        return result
