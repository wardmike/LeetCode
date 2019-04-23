# Prompt: https://leetcode.com/problems/toeplitz-matrix/
# Runtime: 48 ms, faster than 77.63% of Python3 online submissions for Toeplitz Matrix.
# Memory Usage: 13.3 MB, less than 6.86% of Python3 online submissions for Toeplitz Matrix.
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # check diagonals that start at top
        for i in range(len(matrix[0])-1): # -1 because we don't need to check last one (it's a diagonal of 1 element)
            x = i
            y = 0
            val = matrix[0][x]
            # check to see if all in diagonal are the same as this one
            while x < len(matrix[0]) and y < len(matrix):
                if matrix[y][x] != val:
                    return False
                x += 1
                y += 1
        # check diagonals that start at side
        for i in range(len(matrix)-1):
            x = 0
            y = i
            val = matrix[y][0]
            # check to see if all in diagonal are the same as this one
            while x < len(matrix[0]) and y < len(matrix):
                if matrix[y][x] != val:
                    return False
                x += 1
                y += 1
        return True
        
