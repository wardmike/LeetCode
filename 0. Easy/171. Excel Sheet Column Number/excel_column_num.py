# Prompt: https://leetcode.com/problems/excel-sheet-column-number/
# Runtime: 20 ms, faster than 68.97% of Python online submissions for Excel Sheet Column Number.
# Memory Usage: 13.5 MB, less than 57.76% of Python online submissions for Excel Sheet Column Number.


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        reverseColumnTitle = columnTitle[::-1]
        
        multiplier = 1
        total = 0
        for letter in reverseColumnTitle:
            total += multiplier * (ord(letter) - 64)
            multiplier *= 26
        
        return total
