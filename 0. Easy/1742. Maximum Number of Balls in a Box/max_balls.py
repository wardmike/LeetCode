# Prompt: https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
# Runtime: 552 ms, faster than 77.88% of Python online submissions for Maximum Number of Balls in a Box.
# Memory Usage: 16 MB, less than 88.47% of Python online submissions for Maximum Number of Balls in a Box.


class Solution(object):
    
    def sumOfDigits(self, num):
        total = 0
        
        while num > 0:
            total += num % 10
            num /= 10
        
        return total
    
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = {} # maps box number to number of balls in box
        
        for i in range(lowLimit, highLimit+1):
            sumOfDigits = self.sumOfDigits(i)
            
            if sumOfDigits in boxes:
                boxes[sumOfDigits] += 1
            else:
                boxes[sumOfDigits] = 1
        
        return max(list(boxes.values()))
        