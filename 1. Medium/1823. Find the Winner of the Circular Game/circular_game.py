# Prompt: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# Runtime: 32 ms, faster than 100.00% of Python online submissions for Find the Winner of the Circular Game.
# Memory Usage: 13.6 MB, less than 100.00% of Python online submissions for Find the Winner of the Circular Game.


class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        friends = []
        current = -1
        for i in range(1, n+1):
            friends.append(i)

        while len(friends) > 1:
            current += k
            current %= len(friends)
            del friends[current]
            current -= 1 # to account for lost friend
            
        return friends[0]
