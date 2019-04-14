# Prompt: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices):
        holding = False #denotes if stock is currently owned
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i] > prices[i+1] and holding: #sell
                holding = False
                profit += prices[i]
            elif prices[i] < prices[i+1] and not holding: #buy
                holding = True
                profit -= prices[i]
        return profit + prices[-1] if holding else profit #sell on final day if holding
