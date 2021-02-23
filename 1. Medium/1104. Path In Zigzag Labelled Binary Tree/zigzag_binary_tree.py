# Prompt: https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
# Runtime: 28 ms, faster than 21.88% of Python online submissions for Path In Zigzag Labelled Binary Tree.
# Memory Usage: 13.3 MB, less than 95.31% of Python online submissions for Path In Zigzag Labelled Binary Tree.


class Solution(object):
    
    # returns the level that a node is on. level number is determined
    # where the lowest value on the level is 2 ** (level number)
    def getLevel(self, val):
        """
        :type val: int
        :rtype: int
        """
        if val < 1:
            return -1
        level = 0
        nextLevelStart = 2
        
        while val >= nextLevelStart:
            level += 1
            nextLevelStart *= 2
        
        return level
    
    # finds node opposite (mirror image position of) node with value val
    def findOppositeNode(self, val):
        """
        :type val: int
        :rtype: int
        """
        level = self.getLevel(val)
        
        levelStart = 2 ** level
        levelEnd = 2 ** (level + 1) - 1
        
        diffFromStart = val - levelStart
        
        return levelEnd - diffFromStart
        
    
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        # base case
        if label == 1:
            return [1]
        
        # (level / 2) would be parent if alternate rows weren't switched
        parent = self.findOppositeNode(label / 2)
        
        return self.pathInZigZagTree(parent) + [label]
