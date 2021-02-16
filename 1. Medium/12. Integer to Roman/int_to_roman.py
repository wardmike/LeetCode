# Prompt: https://leetcode.com/problems/integer-to-roman/
# Runtime: 40 ms, faster than 63.88% of Python online submissions for Integer to Roman.
# Memory Usage: 13.4 MB, less than 71.88% of Python online submissions for Integer to Roman.


class Solution(object):
    
    def baseToRoman(self, base, fiveBase, tenBase, value):
        """
        :type base: str
        :type halfBase: str
        :type value: int
        :rtype: str
        """
        if value is 4:
            return base + fiveBase
        elif value is 5:
            return fiveBase
        elif value is 9:
            return base + tenBase
        elif value > 5:
            return fiveBase + base * (value - 5)
        else:
            return base * value

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = num / 1000
        num -= (m * 1000)
        c = num / 100
        num -= (c * 100)
        x = num / 10
        num -= (x * 10)
        
        roman = 'M' * m
        
        roman += self.baseToRoman('C', 'D', 'M', c)
        
        roman += self.baseToRoman('X', 'L', 'C', x)
        
        roman += self.baseToRoman('I', 'V', 'X', num)
        
        return roman
