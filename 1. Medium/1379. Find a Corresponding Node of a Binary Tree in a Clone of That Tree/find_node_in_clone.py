# Prompt: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# Runtime: 800 ms, faster than 21.51% of Python online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 30.1 MB, less than 94.85% of Python online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # returns reverse directions to target node (0 - left, 1 - right)
    def findTarget(self, node, target):
        """
        :type node: TreeNode
        :type target: TreeNode
        :rtype: List[int]
        """
        if node == None:
            return []
        elif node == target:
            return [2]
        else:
            leftSide = self.findTarget(node.left, target)
            rightSide = self.findTarget(node.right, target)
            if len(leftSide) != 0:
                leftSide.append(0)
                return leftSide
            if len(rightSide) != 0:
                rightSide.append(1)
                return rightSide
            else:
                return []
            
    def findInClone(self, cloned, path):
        """
        :type cloned: TreeNode
        :type path: List[int]
        :rtype: TreeNode
        """
        for i in path:
            if i == 0:
                cloned = cloned.left
            elif i == 1:
                cloned = cloned.right

        return cloned
        
    
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        # remove the "2" (used for denoting node is found)
        path = self.findTarget(original, target)[1:]
        # reverse "path" to get forward path
        path.reverse()
        
        return self.findInClone(cloned, path)
