# Prompt: https://leetcode.com/problems/richest-customer-wealth/
# Runtime: 40 ms, faster than 55.01% of Python online submissions for Richest Customer Wealth.
# Memory Usage: 13.4 MB, less than 81.28% of Python online submissions for Richest Customer Wealth.
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for customer in accounts:
            customer_total = 0
            for bank in customer:
                customer_total += bank
            if customer_total > richest:
                richest = customer_total
        return richest
