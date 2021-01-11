# Prompt: https://leetcode.com/problems/determine-if-string-halves-are-alike/
# Runtime: 28 ms, faster than 57.23% of Python online submissions for Determine if String Halves Are Alike.
# Memory Usage: 13.6 MB, less than 13.86% of Python online submissions for Determine if String Halves Are Alike.

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # all possible vowels
        vowels = "aeiouAEIOU"
        
        # find first and second halfs
        first = s[:len(s)/2]
        second = s[len(s)/2:]
        
        # find vowels in first half
        first_count = 0
        for i in first:
            if i in vowels:
                first_count += 1
                
        # find vowels in second half
        second_count = 0
        for i in second:
            if i in vowels:
                second_count += 1
                
        return first_count == second_count
