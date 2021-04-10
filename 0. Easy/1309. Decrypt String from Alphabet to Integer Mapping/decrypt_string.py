# Prompt: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Runtime: 24 ms, faster than 31.21% of Python online submissions for Decrypt String from Alphabet to Integer Mapping.
# Memory Usage: 13.5 MB, less than 76.60% of Python online submissions for Decrypt String from Alphabet to Integer Mapping.


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        output = ""
        skip = False
        for i, c in enumerate(s):
            if not skip:
                if c == "1" or "2":
                    if i + 2 < len(s) and s[i+2] == "#":
                        output += chr(int(c+s[i+1]) + 96) # 97 is 'a'
                        skip = True
                        continue
                # not a two-digit number
                if c != "#":
                    output += chr(int(c)+96)
            else:
                skip = False
            
        return output
