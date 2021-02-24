# Prompt: https://leetcode.com/problems/random-pick-index/
# Runtime: 296 ms, faster than 52.28% of Python online submissions for Random Pick Index.
# Memory Usage: 23.1 MB, less than 37.19% of Python online submissions for Random Pick Index.


import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.valToIndices = {} # maps value to indices
        for i, n in enumerate(nums):
            if n in self.valToIndices:
                self.valToIndices[n].append(i)
            else:
                self.valToIndices[n] = [i]
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        possibleIndices = self.valToIndices[target]
        
        i = random.randrange(0, len(possibleIndices))
        return possibleIndices[i]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
