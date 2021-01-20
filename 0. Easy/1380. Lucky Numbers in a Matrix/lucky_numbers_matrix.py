# Prompt: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# Runtime: 104 ms, faster than 73.71% of Python online submissions for Lucky Numbers in a Matrix.
# Memory Usage: 13.8 MB, less than 27.89% of Python online submissions for Lucky Numbers in a Matrix.


class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        minRows = []
        luckyNumbers = []
        for row in matrix:
            minRows.append(min(row))
            
        maxCols = []
        for i in range(len(matrix[0])):
            mx = matrix[0][i]
            for j in range(len(matrix)):
                if matrix[j][i] > mx:
                    mx = matrix[j][i]
            maxCols.append(mx)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if minRows[i] == matrix[i][j] and maxCols[j] == matrix[i][j]:
                    luckyNumbers.append(matrix[i][j])
        
        return luckyNumbers
