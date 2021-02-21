# Prompt: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Runtime: 48 ms, faster than 21.54% of Python online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 13.4 MB, less than 61.75% of Python online submissions for Find Numbers with Even Number of Digits.


class Solution(object):
    
    def findNumDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numDigits = 0
        while num > 0:
            num /= 10
            numDigits += 1
        
        return numDigits
    
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numWithEvenDigits = 0
        
        for num in nums:
            numDigits = self.findNumDigits(num)
            if numDigits % 2 == 0:
                numWithEvenDigits += 1
        
        return numWithEvenDigits
