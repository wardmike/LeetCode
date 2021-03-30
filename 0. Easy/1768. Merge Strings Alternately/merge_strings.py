# Prompt: https://leetcode.com/problems/merge-strings-alternately/
# Runtime: 16 ms, faster than 82.61% of Python online submissions for Merge Strings Alternately.
# Memory Usage: 13.4 MB, less than 66.23% of Python online submissions for Merge Strings Alternately.


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = []
        
        longer = len(word1) if len(word1) > len(word2) else len(word2)
        
        for i in range(longer):
            if i < len(word1):
                merge.append(word1[i])
            if i < len(word2):
                merge.append(word2[i])  

        return ''.join(merge)
