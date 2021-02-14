# Prompt: https://leetcode.com/problems/detect-capital/
# Runtime: 20 ms, faster than 62.75% of Python online submissions for Detect Capital.
# Memory Usage: 13.3 MB, less than 87.58% of Python online submissions for Detect Capital.


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        
        if len(word) < 2:
            return True
        
        if word[0] in upper:
            if word[1] in upper:
                # should be all-caps
                for i in range(2, len(word)):
                    if word[i] in lower:
                        return False
            else:
                # should be all lower except for word[0]
                for i in range(2, len(word)):
                    if word[i] in upper:
                        return False
        else:
            # should be all lower
            for i in range(1, len(word)):
                if word[i] in upper:
                    return False
        
        return True    
