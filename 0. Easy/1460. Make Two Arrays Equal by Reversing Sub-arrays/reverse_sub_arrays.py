# Prompt: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
# Runtime: 92 ms, faster than 21.10% of Python online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
# Memory Usage: 13.6 MB, less than 85.05% of Python online submissions for Make Two Arrays Equal by Reversing Sub-arrays.

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        # arrays can become equal by reversing sub-arrays iff they both contain
        # the same values. Since there are unlimited steps to reverse sub-arrays,
        # any possible rearrangement can be done

        target.sort()
        arr.sort()
        
        return target == arr
