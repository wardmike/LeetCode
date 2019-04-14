"""
PROMPT: Give a string s, count the number of non-empty (contiguous) substrings that have
the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are
grouped consecutively. Substrings that occur multiple times are counted the number of
times they occur.
"""
class Solution(object):
    def countBinarySubstrings(self, s):
        zz = 0 # count of zeros
        oo = 0 # count of ones
        on_zero = (int(s[0]) == 0) #shows if current digit is 0
        t = 0 #total count
        for j in s:
            i = int(j)
            #check for digit switch and update total count
            if (i == 0) != on_zero:
                on_zero = (i == 0)
                t += min(oo, zz)
                if on_zero:
                    zz = 0
                else:
                    oo = 0
            #increment 0s or 1s counter
            if i == 0:
                zz += 1
            else:
                oo += 1
        t += min(oo, zz) #add for last group of 0s or 1s
        return t
