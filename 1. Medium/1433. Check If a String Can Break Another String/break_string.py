# Prompt: https://leetcode.com/problems/check-if-a-string-can-break-another-string/
# Runtime: 368 ms, faster than 13.89% of Python online submissions for Check If a String Can Break Another String.
# Memory Usage: 19.9 MB, less than 41.67% of Python online submissions for Check If a String Can Break Another String.

class Solution(object):
    
    # tries to see if s2 can break s1
    def tryBreak(self, s1, s2):
        """
        :type s1: List[str]
        :type s2: List[str]
        :rtype: bool
        """
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                return False
        return True
    
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # sorting and then comparing one by one is the easiest
        # way to see if one can break the other
        s1 = sorted(s1)
        s2 = sorted(s2)
        return self.tryBreak(s1, s2) or self.tryBreak(s2, s1)
