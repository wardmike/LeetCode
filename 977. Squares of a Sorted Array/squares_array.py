# Prompt: https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, A):
        # This could probably be improved by splitting the negatives into a separate array
        # and sorting those before adding to the positive array. This would save sort time
        # because the positive ones don't need to be sorted. Not sure if Python's sort()
        # is optimized enough be the same speed as that solution would be.
        A2 = [x**2 for x in A]
        A2.sort()
        return A2
        
