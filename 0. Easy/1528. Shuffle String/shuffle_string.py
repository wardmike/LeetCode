# Prompt: https://leetcode.com/problems/shuffle-string/
# Runtime: 40 ms, faster than 70.86% of Python online submissions for Shuffle String.
# Memory Usage: 13.4 MB, less than 69.33% of Python online submissions for Shuffle String.


class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
        keys = {} # maps indices to letters
        for i, val in enumerate(indices):
            keys[val] = s[i]
        
        word = ""
        for key in keys:
            word += keys[key]
            
        return word
