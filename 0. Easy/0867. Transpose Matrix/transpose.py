# Prompt: https://leetcode.com/problems/transpose-matrix
"""
 Notes: could make this have better memory usage if we swapped in place
 instead of making new lists, but that gets a little tricky with changing
 sizes.
"""
# Runtime: 64 ms, faster than 62.65% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 13.6 MB, less than 5.45% of Python3 online submissions for Transpose Matrix.
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        A1 = [] # transposed matrix
        height = len(A)
        width = len(A[0])
        for x in range(width):
            A11 = [] # one row of the transposed matrix
            for y in range(height):
                A11.append(A[y][x])
            A1.append(A11)
        return A1
