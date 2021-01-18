# Prompt: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Runtime: 16 ms, faster than 86.82% of Python online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 13.3 MB, less than 87.11% of Python online submissions for Minimum Add to Make Parentheses Valid.

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        countOpen = 0
        countClosed = 0
        
        for s in S:
            if s == "(":
                countOpen += 1
            elif s == ")":
                if countOpen > 0:
                    # matches an existing open
                    countOpen -= 1
                else:
                    countClosed += 1
        
        return countOpen + countClosed
