# Prompt: https://leetcode.com/problems/game-of-life/
# Runtime: 12 ms, faster than 98.56% of Python online submissions for Game of Life.
# Memory Usage: 13.6 MB, less than 18.74% of Python online submissions for Game of Life.


class Solution(object):
    
    # returns the number of live neighbors at position (m, n)
    def numNeighbors(self, board, m, n):
        neighbors = 0
        
        # upper left
        if m > 0 and n > 0:
            if board[m-1][n-1] % 2 == 1: # 3 represents a 1 being turned into a 0
                neighbors += 1
        # straight above
        if m > 0:
            if board[m-1][n] % 2 == 1:
                neighbors += 1
        # upper right
        if m > 0 and n < len(board[0]) - 1:
            if board[m-1][n+1] % 2 == 1:
                neighbors += 1
        # straight right
        if n < len(board[0]) - 1:
            if board[m][n+1] % 2 == 1:
                neighbors += 1
        # bottom right
        if m < len(board) - 1 and n < len(board[0]) - 1:
            if board[m+1][n+1] % 2 == 1:
                neighbors += 1
        # straight down
        if m < len(board) - 1:
            if board[m+1][n] % 2 == 1:
                neighbors += 1
        # bottom left
        if m < len(board) - 1 and n > 0:
            if board[m+1][n-1] % 2 == 1:
                neighbors += 1
        # straight left
        if n > 0:
            if board[m][n-1] % 2 == 1:
                neighbors += 1
        
        return neighbors
            
    
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # 2 represents a 0 being turned into a 1
        # 3 represents a 1 being turned into a 0
        
        
        for m, row in enumerate(board):
            for n, cell in enumerate(row):
                neighbors = self.numNeighbors(board, m, n)
                
                if cell == 0 and neighbors == 3:
                    board[m][n] = 2
                elif cell == 1 and neighbors != 2 and neighbors != 3:
                    board[m][n] = 3
            
        # change 2's to 1's and 3's to 0's
        
        for m, row in enumerate(board):
            for n, cell in enumerate(row):
                if cell == 2:
                    board[m][n] = 1
                elif cell == 3:
                    board[m][n] = 0
