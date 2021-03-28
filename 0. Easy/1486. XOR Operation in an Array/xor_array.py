# Prompt: https://leetcode.com/problems/xor-operation-in-an-array/
# Runtime: 20 ms, faster than 47.83% of Python online submissions for XOR Operation in an Array.
# Memory Usage: 13.5 MB, less than 48.43% of Python online submissions for XOR Operation in an Array.


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        current = start
        xor = current
        
        for i in range(n-1):
            current += 2
            xor = xor ^ current
        
        return xor
