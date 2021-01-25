# Prompt: https://leetcode.com/problems/queens-that-can-attack-the-king/
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Queens That Can Attack the King.
# Memory Usage: 13.7 MB, less than 26.87% of Python online submissions for Queens That Can Attack the King.

class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        
        queenSet = set()
        for pos in queens:
            # because coordinates run from 0 to 8, they can be concatenated together and remain unique
            queenSet.add(str(pos[0]) + str(pos[1]))
        
        # try moving away from king in all dimensions
        output = []
        # up
        
        i = king[0] - 1
        while i >= 0:
            if str(i) + str(king[1]) in queenSet:
                output.append([i, king[1]])
                break # break loop because any queens farther along in this direction are blocked by this queen
            i -= 1
        
        # down
        i = king[0] + 1
        while i < 9:
            if str(i) + str(king[1]) in queenSet:
                output.append([i, king[1]])
                break
            i += 1
            
        # left
        i = king[1] - 1
        while i >= 0:
            if str(king[0]) + str(i) in queenSet:
                output.append([king[0], i])
                break
            i -= 1
            
        # right
        i = king[1] + 1
        while i < 9:
            if str(king[0]) + str(i) in queenSet:
                output.append([king[0], i])
                break
            i += 1
        
        # diagonal - up & left
        i = king[0] - 1
        j = king[1] - 1
        while i >= 0 and j >= 0:
            if str(i) + str(j) in queenSet:
                output.append([i, j])
                break
            i -= 1
            j -= 1
            
        # diagonal - up & right
        i = king[0] - 1
        j = king[1] + 1
        while i >= 0 and j < 9:
            if str(i) + str(j) in queenSet:
                output.append([i, j])
                break
            i -= 1
            j += 1
        
        # diagonal - down & right
        i = king[0] + 1
        j = king[1] + 1
        while i < 9 and j < 9:
            if str(i) + str(j) in queenSet:
                output.append([i, j])
                break
            i += 1
            j += 1
            
        # diagonal - down & left
        i = king[0] + 1
        j = king[1] - 1
        while i < 9 and j >= 0:
            if str(i) + str(j) in queenSet:
                output.append([i, j])
                break
            i += 1
            j -= 1
            
        return output
