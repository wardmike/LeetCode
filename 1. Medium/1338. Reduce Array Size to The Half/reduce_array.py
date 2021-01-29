# Prompt: https://leetcode.com/problems/reduce-array-size-to-the-half/
# Runtime: 716 ms, faster than 25.23% of Python online submissions for Reduce Array Size to The Half.
# Memory Usage: 28.4 MB, less than 90.99% of Python online submissions for Reduce Array Size to The Half.

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # dict of integers to number of occurrences
        occurrences = {}
        # populate dict
        for i in arr:
            if i in occurrences:
                occurrences[i] += 1
            else:
                occurrences[i] = 1
        
        # represents numbers of occurrences
        vals = occurrences.values()
        # sort big to small because we want min size of set
        vals.sort(reverse=True)
        
        half = len(arr) / 2
        totalSoFar = 0
        
        # keep "adding to set" until >= half is reached
        for i, val in enumerate(vals):
            totalSoFar += val
            if totalSoFar >= half:
                return i+1
        return 0
