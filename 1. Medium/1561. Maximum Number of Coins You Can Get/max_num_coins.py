# Prompt: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
# Runtime: 696 ms, faster than 25.00% of Python online submissions for Maximum Number of Coins You Can Get.
# Memory Usage: 23.4 MB, less than 37.16% of Python online submissions for Maximum Number of Coins You Can Get.

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        # sort
        piles.sort(reverse=True)
        
        # pick
        picks = len(piles) / 3
        total = 0
        # take every other coin starting with 2nd
        for i in range(0, picks):
            total += piles[(2 * i) + 1]
        
        return total
