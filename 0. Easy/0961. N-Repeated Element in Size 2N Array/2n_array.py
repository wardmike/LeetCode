# Prompt: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
class Solution:
    def repeatedNTimes(self, A):
        unique = {} #dictionary lookup time is O(1)
        for a in A:
            if a in unique:
                return a #only one element occurs more than once
            else:
                unique[a] = 1
