# Prompt: https://leetcode.com/problems/minesweeper/
# Runtime: 156 ms, faster than 74.82% of Python online submissions for Minesweeper.
# Memory Usage: 15.6 MB, less than 48.58% of Python online submissions for Minesweeper.

class Solution(object):
    def __init__(self):
        self.done = False
    
    # returns true if char is a mine (revealed or unrevealed); returns false if not
    def isMine(self, char):
        """
        :type char: str
        :rtype: bool
        """
        return (char == "M" or char == "X")
    
    # checks adjacent squares for mines and returns value for square
    def checkAdjacent(self, board, i, j):
        """
        :type board: List[List[str]]
        :type i: int
        :type j: int
        :rtype: int or str
        """
        num = 0
        
        # up
        if i > 0 and self.isMine(board[i-1][j]):
            num += 1
        # down
        if i < len(board) - 1 and self.isMine(board[i+1][j]):
            num += 1
        # left
        if j > 0 and self.isMine(board[i][j-1]):
            num += 1
        # right
        if j < len(board[0]) - 1 and self.isMine(board[i][j+1]):
            num += 1
        # up & left
        if i > 0 and j > 0 and self.isMine(board[i-1][j-1]):
            num += 1
        # up & right
        if i > 0 and j < len(board[0]) - 1 and self.isMine(board[i-1][j+1]):
            num += 1
        # down & left
        if i < len(board) - 1 and j > 0 and self.isMine(board[i+1][j-1]):
            num += 1
        # down & right
        if i < len(board) - 1 and j < len(board[0]) - 1 and self.isMine(board[i+1][j+1]):
            num += 1
        
        return str(num) if num > 0 else "B"
    
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # prase input
        i = click[0]
        j = click[1]
        
        # out of bounds; return
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or self.done:
            return board
        
        # check if mine
        if board[i][j] == "M":
            board[i][j] = "X"
            self.done = True
            return board
        elif board[i][j] == "E":
            adj = self.checkAdjacent(board, i, j)
            board[i][j] = adj
            if adj != "B":
                return board
        else: # a space that has already been seen
            return board
        
        # recursively call neighbors (will have returned before if we don't want to check)
        self.updateBoard(board, [i-1, j])
        self.updateBoard(board, [i+1, j])
        self.updateBoard(board, [i, j-1])
        self.updateBoard(board, [i, j+1])
        self.updateBoard(board, [i-1, j-1])
        self.updateBoard(board, [i-1, j+1])
        self.updateBoard(board, [i+1, j-1])
        self.updateBoard(board, [i+1, j+1])
            
        return board
