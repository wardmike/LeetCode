# https://leetcode.com/problems/battleships-in-a-board/
# Runtime: 40 ms, faster than 82.31% of Python3 online submissions for Battleships in a Board.
# Memory Usage: 13.5 MB, less than 5.09% of Python3 online submissions for Battleships in a Board.
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    # if there is no "X" above or to the left, we haven't counted this ship yet
                    if i== 0 or board[i-1][j] != "X":
                        if j == 0 or board[i][j-1] != "X":
                            count += 1
        return count
