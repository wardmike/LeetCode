# Prompt: https://leetcode.com/problems/rotting-oranges/submissions/
class Solution:
    # returns whether or not the orange has a rotten neighbor
    def hasRottenNeighbor(self, grid, i, j):
        if i > 0 and grid[i-1][j] == 2:
            return True
        elif i < len(grid) - 1 and grid[i+1][j] == 2:
            return True
        elif j > 0 and grid[i][j-1] == 2:
            return True
        elif j < len(grid[i]) - 1 and grid[i][j+1] == 2:
            return True
        else:
            return False
        
    # change temporary values to rotten
    def changeTemp(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 3:
                    grid[i][j] = 2
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        done = False
        count = 0
        changed = False
        foundNotRotten = False
        while not done:
            count += 1
            done = True
            changed = False
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        foundNotRotten = True
                        if self.hasRottenNeighbor(grid, i, j):
                            #set to temp value so it doesn't make neighbors rotten this turn
                            grid[i][j] = 3
                            changed = True
                        else: #we found a non-rotten orange, so we will continue to next turn
                            done = False
            self.changeTemp(grid)
            if not changed: #nothing can be changed in this grid
                if foundNotRotten:
                    return -1 #some are found that will never become rotten
                else:
                    return 0 #all oranges are rotten
        return count
            
