# Prompt: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
# Runtime: 12 ms, faster than 93.55% of Python online submissions for Generate a String With Characters That Have Odd Counts.
# Memory Usage: 13.3 MB, less than 92.26% of Python online submissions for Generate a String With Characters That Have Odd Counts.


class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n % 2 == 1:
            return "a" * n
        else:
            return "a" * (n-1) + "b"
