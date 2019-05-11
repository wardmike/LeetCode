# Prompt: https://leetcode.com/problems/reverse-bits

# Runtime: 28 ms, faster than 25.07% of Python online submissions for Reverse Bits.
# Memory Usage: 11.8 MB, less than 5.38% of Python online submissions for Reverse Bits.

from array import array

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse = array("B")
        while n.bit_length() > 0:
            reverse.append(n & 1)
            n >>= 1
        # append zeroes to the end
        while len(reverse) < 32:
            reverse.append(0)
        return reduce(lambda m, n: (m << 1) + n, reverse, 0)
        
