# Prompt: https://leetcode.com/problems/apply-discount-every-n-orders/
# Runtime: 636 ms, faster than 100.00% of Python online submissions for Apply Discount Every n Orders.
# Memory Usage: 19.6 MB, less than 36.59% of Python online submissions for Apply Discount Every n Orders.


class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.count = 0
        self.discount = discount
        self.prices = {} # maps product id to price
        for i, product in enumerate(products):
            self.prices[product] = prices[i]
        

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        # calculate cost
        total = 0
        for i, p in enumerate(product):
            price = self.prices[p]
            total += price * amount[i]
        
        self.count += 1
        # apply discount (if applicable)
        if self.count == self.n:
            self.count = 0
            
            # apply discount
            
            total = total - (self.discount * total) / 100.0
        
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
