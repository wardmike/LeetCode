# Prompt: https://leetcode.com/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: 'str', typed: 'str') -> 'bool':
        ii = 0 #index for traversing variable "name"
        for i in typed:
            if ii < len(name) and i == name[ii]: #letter is correct
                ii += 1
                continue
            elif ii > 0 and i == name[ii-1]: #letter is long pressed
                continue
            else: #letter is wrong
                return False
        #only return true if ii has traversed the entire string
        return ii == len(name)
