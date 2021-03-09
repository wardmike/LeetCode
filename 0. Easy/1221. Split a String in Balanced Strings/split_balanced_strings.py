# Prompt: https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Runtime: 12 ms, faster than 96.32% of Python online submissions for Split a String in Balanced Strings.
# Memory Usage: 13.4 MB, less than 87.86% of Python online submissions for Split a String in Balanced Strings.


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ratio = 0 # l - r
        
        output = 0 # num of balanced strings
        
        for d in s:
            if d == "L":
                ratio += 1
            elif d == "R":
                ratio -= 1
            
            if ratio == 0:
                output += 1
        
        return output
