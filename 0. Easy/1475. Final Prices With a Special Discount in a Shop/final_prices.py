# Prompt: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Runtime: 56 ms, faster than 38.93% of Python online submissions for Final Prices With a Special Discount in a Shop.
# Memory Usage: 13.4 MB, less than 75.84% of Python online submissions for Final Prices With a Special Discount in a Shop.

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        final = []
        
        for i, val in enumerate(prices):
            # find j
            foundJ = False
            for j in range(i+1, len(prices)):
                if prices[j] <= val:
                    final.append(val - prices[j])
                    foundJ = True
                    break
            if not foundJ:
                final.append(val)
                
        return final
