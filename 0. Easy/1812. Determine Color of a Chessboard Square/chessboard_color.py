# Prompt: https://leetcode.com/problems/determine-color-of-a-chessboard-square/
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Determine Color of a Chessboard Square.
# Memory Usage: 13.7 MB, less than 100.00% of Python online submissions for Determine Color of a Chessboard Square.


class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        col = coordinates[0]
        row = coordinates[1]

        # adding the row num to a numeric value for the col (starting with "a" being odd)
        # will give us even if the square is black and odd if it is white
        return (ord(col) + int(row)) % 2 == 1
