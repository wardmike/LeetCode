# Prompt: https://leetcode.com/problems/maximum-69-number/
# Runtime: 16 ms, faster than 75.80% of Python online submissions for Maximum 69 Number.
# Memory Usage: 13.7 MB, less than 13.38% of Python online submissions for Maximum 69 Number.


class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # change the first 6 to a 9
        newNum = ""
        changed = False
        
        for digit in str(num):
            if digit == "6" and not changed:
                newNum += "9"
                changed = True
            else:
                newNum += digit
        return int(newNum)
