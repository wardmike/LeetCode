# Prompt: https://leetcode.com/problems/binary-gap

# Runtime: 36 ms, faster than 99.42% of Python3 online submissions for Binary Gap.
# Memory Usage: 13 MB, less than 6.67% of Python3 online submissions for Binary Gap.

class Solution:
    def binaryGap(self, N: int) -> int:
        binary = "{0:b}".format(N)
        
        biggestDist = 0
        currentDist = -1 # -1 denotes that we haven't found any 1 yet
        for bit in binary:
            if currentDist == -1:
                if bit == '1':
                    currentDist = 1
            elif bit == '0':
                currentDist += 1
            else:
                if currentDist > biggestDist:
                    biggestDist = currentDist
                currentDist = 1
        
        return biggestDist
