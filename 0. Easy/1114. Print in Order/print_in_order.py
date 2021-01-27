# Prompt: https://leetcode.com/problems/print-in-order/
# Runtime: 40 ms, faster than 46.55% of Python online submissions for Print in Order.
# Memory Usage: 13.7 MB, less than 29.31% of Python online submissions for Print in Order.

import time

class Foo(object):
    def __init__(self):
        self.lastPrinted = 0

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lastPrinted = 1

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        while self.lastPrinted != 1:
            time.sleep(0.1)
        printSecond()
        self.lastPrinted = 2   
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        # printThird() outputs "third". Do not change or remove this line.
        while self.lastPrinted != 2:
            time.sleep(0.1)
        printThird()
