# Prompt: https://leetcode.com/problems/jump-game-iii/
# Runtime: 360 ms, faster than 10.10% of Python online submissions for Jump Game III.
# Memory Usage: 20.8 MB, less than 48.56% of Python online submissions for Jump Game III.

class Solution(object):
    
    # visits an index and returns the possible jumps from that index
    def visitIndex(self, arr, idx, visited):
        """
        :type arr: List[int]
        :type idx: int
        :type visited: set
        :rtype: bool
        """
        visited.add(idx)
        
        leftJump = idx - arr[idx]
        rightJump = idx + arr[idx]
        
        possibleJumps = []
        
        # check that jumps are valid
        if leftJump >= 0:
            possibleJumps.append(leftJump)
            
        if rightJump < len(arr):
            possibleJumps.append(rightJump)
            
        return possibleJumps
    
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = set()
        queue = [start]
        
        while len(queue) > 0:
            nextIdx = queue.pop(0)
            if nextIdx not in visited: # prevent going to the same place twice
                if arr[nextIdx] == 0:
                    return True
                queue += self.visitIndex(arr, nextIdx, visited)
                
        return False
