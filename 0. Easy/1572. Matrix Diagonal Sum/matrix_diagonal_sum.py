# Prompt: https://leetcode.com/problems/matrix-diagonal-sum/
# Runtime: 88 ms, faster than 55.68% of Python online submissions for Matrix Diagonal Sum.
# Memory Usage: 13.6 MB, less than 44.32% of Python online submissions for Matrix Diagonal Sum.


class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sm = 0
        length = len(mat)
        for i in range(length):
            sm += mat[i][i]
            # avoid adding middle twice
            if i != length-i-1:
                sm += mat[length-i-1][i]
                
        return sm
