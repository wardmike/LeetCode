# Prompt: https://leetcode.com/problems/available-captures-for-rook/submissions/
class Solution:
    
    def findRook(self, board):
        for y in range(len(board)): #traverse rows
            for x in range(len(board[y])):
                if board[y][x] == "R":
                    return x,y
        return -1,-1
    
    def numRookCaptures(self, board: List[List[str]]) -> int:
        #find rook's position
        rook_x, rook_y = self.findRook(board)
        
        # go out in each direction and see if the rook can capture a pawn in that direction
        can_capture = 0 #pawns the rook can capture
        # up
        for y in range(rook_y-1, -1, -1):
            if board[y][rook_x] == 'p':
                can_capture += 1
            if board[y][rook_x] != '.':
                break
        # down
        for y in range(rook_y+1, 8):
            if board[y][rook_x] == 'p':
                can_capture += 1
            if board[y][rook_x] != '.':
                break
        # left
        for x in range(rook_x-1, -1, -1):
            if board[rook_y][x] == 'p':
                can_capture += 1
            if board[rook_y][x] != '.':
                break
        # right
        for x in range(rook_x+1, 8):
            if board[rook_y][x] == 'p':
                can_capture += 1
            if board[rook_y][x] != '.':
                break
        
        return can_capture
