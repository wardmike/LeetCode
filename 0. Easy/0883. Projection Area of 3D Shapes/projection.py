# Prompt: https://leetcode.com/problems/projection-area-of-3d-shapes/submissions/
class Solution:
    def projectionArea(self, grid: 'List[List[int]]') -> 'int':        
        total = 0
        num = 0 #number of towers; used for top view
        #calculate along the x-axis
        for i in range(len(grid)):
            tallest = 0
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    num += 1
                    if grid[i][j] > tallest:
                        tallest = grid[i][j]
            total += tallest
        
        #calculate along the y-axis
        for j in range(len(grid)):
            tallest = 0
            for i in range(len(grid[0])): #prompt says length = width
                if grid[i][j] > tallest:
                    tallest = grid[i][j]
            total += tallest            
        
        return total + num
