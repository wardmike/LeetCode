# Prompt: https://leetcode.com/problems/simplified-fractions/
# Runtime: 584 ms, faster than 29.27% of Python online submissions for Simplified Fractions.
# Memory Usage: 14 MB, less than 51.22% of Python online submissions for Simplified Fractions.


class Solution(object):
    
    def isFractionSimplified(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: boolean
        """
        for i in range(2, denominator+1): # n can only be between 1 and 100
            if numerator % i == 0 and denominator % i == 0:
                return False
        return True
        
    
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        total = []
        for numerator in range(1, n):
            for denominator in range(2, n+1):
                if numerator < denominator:
                    if self.isFractionSimplified(numerator, denominator):
                        total.append(str(numerator) + "/" + str(denominator))
        
        return total
