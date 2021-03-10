# Prompt: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# Runtime: 212 ms, faster than 82.43% of Python online submissions for Minimum Number of Steps to Make Two Strings Anagram.
# Memory Usage: 14.5 MB, less than 39.53% of Python online submissions for Minimum Number of Steps to Make Two Strings Anagram.


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        sMap = {} # maps letters to num of occurrences
        
        for letter in s:
            if letter in sMap:
                sMap[letter] += 1
            else:
                sMap[letter] = 1
        
        toChange = 0
        for letter in t:
            if letter in sMap:
                if sMap[letter] <= 0:
                    toChange += 1
                else:
                    sMap[letter] -= 1
            else:
                toChange += 1
                
        return toChange
