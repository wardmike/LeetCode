# Prompt: https://leetcode.com/problems/sort-integers-by-the-power-value/
# Runtime: 768 ms, faster than 39.39% of Python online submissions for Sort Integers by The Power Value.
# Memory Usage: 13.4 MB, less than 89.90% of Python online submissions for Sort Integers by The Power Value.


class Solution(object):
    
    def getPower(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 1:
            steps += 1
            if num % 2 == 0:
                num = num / 2
            else:
                num = 3 * num + 1
        
        return steps
            
    
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        powers = {} # maps number to power
        for i in range(lo, hi+1):
            powers[i] = self.getPower(i)
        
        nums = range(lo, hi+1)
        sortedNums = sorted(nums, key=lambda n:(powers[n], n))
        
        return sortedNums[k-1] # k is 1-indexed
