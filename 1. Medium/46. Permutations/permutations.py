# Prompt: https://leetcode.com/problems/permutations/
# Runtime: 28 ms, faster than 69.13% of Python online submissions for Permutations.
# Memory Usage: 13.6 MB, less than 68.98% of Python online submissions for Permutations.


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        
        permutations = []
        
        # get all permutations of nums without n & then add n to the beginning of all of them
        for i, n in enumerate(nums):
            temp = []
            
            substr_permutations = self.permute(nums[:i] + nums[i+1:])
            for s in substr_permutations:
                temp.append([n] + s)
            
            permutations += temp
        
        return permutations
