# Prompt: https://leetcode.com/problems/the-kth-factor-of-n/
# Runtime: 20 ms, faster than 74.16% of Python online submissions for The kth Factor of n.
# Memory Usage: 13.5 MB, less than 36.70% of Python online submissions for The kth Factor of n.


class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        i = 0
        
        for num in range(1, n+1):
            if n % num == 0:
                i += 1
            if i == k:
                return num
        
        return -1
