# Prompt: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# Runtime: 16 ms, faster than 93.15% of Python online submissions for Calculate Money in Leetcode Bank.
# Memory Usage: 13.6 MB, less than 9.52% of Python online submissions for Calculate Money in Leetcode Bank.

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = int(n / 7)
        remainder = n % 7
        
        # add (1 + 2 + 3 + 4 + 5 + 6 + 7) for each week
        money = weeks * 28
        
        # add difference accounting for each week having +7 more than week before
        money += weeks * (weeks - 1) / 2 * 7
        
        # add remainder
        for i in range(remainder):
            money += (weeks + 1) + i
        
        return money
