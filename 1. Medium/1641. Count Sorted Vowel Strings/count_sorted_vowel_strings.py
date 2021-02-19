# Prompt: https://leetcode.com/problems/count-sorted-vowel-strings/
# Runtime: 12 ms, faster than 97.01% of Python online submissions for Count Sorted Vowel Strings.
# Memory Usage: 13.3 MB, less than 74.97% of Python online submissions for Count Sorted Vowel Strings.


class Solution(object):
    
    # returns an array of the count of strings of length n that start with 
    # ["a","e","i","o","u"] respectively
    def findVowelCounts(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [1, 1, 1, 1, 1]
        else:
            prev = self.findVowelCounts(n-1)
            # "a" can be put before each string of length n-1
            a = sum(prev)
            # "e" can be put before every string that doesn't start with a
            e = prev[1] + prev[2] + prev[3] + prev[4]
            # "i" can be put before every string that doesn't start with a or e
            i = prev[2] + prev[3] + prev[4]
            # "o" can be put before every string that doesn't start with a, e, or i
            o = prev[3] + prev[4]
            # there's always only one string of length n that starts with u (u repeated n times)
            u = 1
            return [a, e, i, o, u]
    
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # sum all the strings of length n
        return sum(self.findVowelCounts(n))
