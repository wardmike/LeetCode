# Prompt: https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 40 ms, faster than 95.34% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13.4 MB, less than 7.71% of Python3 online submissions for Symmetric Tree.

class Solution:
    # takes two nodes (one for each side of the tree) & recursively calls opposite sides on each
    # the tree is symmetric if each left from node1 equals a right from node2 and vice versa
    def isSymmetricRecursive(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 != None and node2 != None and node1.val == node2.val:
            path1Symmetric = self.isSymmetricRecursive(node1.left, node2.right)
            path2Symmetric = self.isSymmetricRecursive(node1.right, node2.left)
            return (path1Symmetric and path2Symmetric)
        elif node1 == None and node2 == None:
            return True
        else:
            return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isSymmetricRecursive(root.left, root.right)
