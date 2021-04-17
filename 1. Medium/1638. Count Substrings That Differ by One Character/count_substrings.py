# Prompt: https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
# Runtime: 4256 ms, faster than 6.90% of Python online submissions for Count Substrings That Differ by One Character.
# Memory Usage: 15.3 MB, less than 13.79% of Python online submissions for Count Substrings That Differ by One Character.


class Solution(object):
    
    def differByOne(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        
        # returns true iff a and b differ by one character
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        
        return diff == 1
    
    
    def getAllSubstr(self, s):
        """
        :type s: str
        :rtype: dict
        """
        # returns dict that maps length to substrs of that length
        
        substrs = {}
        for length in range(1, len(s)+1):
            substrs[length] = []
            for i in range(len(s)-length+1):
                substrs[length].append(s[i:i+length])
                
        return substrs
                
    
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        count = 0
        sSubstrs = self.getAllSubstr(s)
        tSubstrs = self.getAllSubstr(t)
        
        biggerLen = len(s) if len(s) > len(t) else len(t)
            
        for l in range(biggerLen+1):
            if l in sSubstrs and l in tSubstrs:
                for ss in sSubstrs[l]:
                    for tt in tSubstrs[l]:
                        count += self.differByOne(ss, tt)
        
                
        return count 
