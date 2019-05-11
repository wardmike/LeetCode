# Prompt: https://leetcode.com/problems/happy-number

# Runtime: 36 ms, faster than 99.50% of Python3 online submissions for Happy Number.
# Memory Usage: 13.1 MB, less than 5.29% of Python3 online submissions for Happy Number.

class Solution:
    def getDigitsSquaredSum(self, n: int) -> int:
        # break it into digits
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = int(n / 10)
        # square & sum them
        total = 0
        for digit in digits:
            total += digit * digit        
        return int(total)
    
    def isHappy(self, n: int) -> bool:
        previousNumbers = set()
        while n not in previousNumbers:
            previousNumbers.add(n)
            n = self.getDigitsSquaredSum(n)
            if n == 1:
                return True
        return False
        
