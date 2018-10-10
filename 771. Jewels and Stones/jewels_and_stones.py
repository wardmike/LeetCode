class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        for i in S:
            if i in J:
                count += 1
        return count
