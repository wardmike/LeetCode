# Prompt: https://leetcode.com/problems/thousand-separator/
# Runtime: 16 ms, faster than 69.70% of Python online submissions for Thousand Separator.
# Memory Usage: 13.3 MB, less than 89.70% of Python online submissions for Thousand Separator.


class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = str(n)
        nLen = len(n)
        
        i = 1 # can't add before first one
        while i < nLen - 2: # last two won't have a dot
            if (nLen - i) % 3 == 0:
                n = n[:i] + "." + n[i:]
                
                # increment to account for dot added
                i += 1
                nLen += 1
            i += 1
            
        return n
