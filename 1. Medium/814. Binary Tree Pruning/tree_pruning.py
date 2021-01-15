# Prompt: https://leetcode.com/problems/binary-tree-pruning/
# Runtime: 12 ms, faster than 96.86% of Python online submissions for Binary Tree Pruning.
# Memory Usage: 13.4 MB, less than 69.06% of Python online submissions for Binary Tree Pruning.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isLeaf(self, node):
        """
        :type node: TreeNode
        :rtype: boolean
        """
        return (node.left == None and node.right == None)
    
    def removeAllLeafZeros(self, node):
        """
        :type node: TreeNode
        :rtype: boolean
        """
        changed = False
        changedLeft = False
        changedRight = False
        if node.left != None:
            if self.isLeaf(node.left):
                if node.left.val == 0:
                    node.left = None
                    changed = True
            else:
                changedLeft = self.removeAllLeafZeros(node.left)
        
        if node.right != None:
            if self.isLeaf(node.right):
                if node.right.val == 0:
                    node.right = None
                    changed = True
            else:
                changedRight = self.removeAllLeafZeros(node.right)
                
        return (changed or changedLeft or changedRight)
        
    
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if self.isLeaf(root) and root.val == 0:
            return None
        
        changed = self.removeAllLeafZeros(root)
        
        while changed:
            changed = self.removeAllLeafZeros(root)
            if self.isLeaf(root) and root.val == 0:
                return None
            
        return root
