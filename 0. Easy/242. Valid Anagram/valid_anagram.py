# Prompt: https://leetcode.com/problems/valid-anagram/
# Runtime: 48 ms, faster than 51.99% of Python online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 43.17% of Python online submissions for Valid Anagram.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return sorted(s) == sorted(t)
