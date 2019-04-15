# Prompt: https://leetcode.com/problems/univalued-binary-tree
"""
 Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
"""
# Runtime: 36 ms, faster than 89.88% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 13.2 MB, less than 5.36% of Python3 online submissions for Univalued Binary Tree.
class Solution:
    def isUnivalTreeNode(self, node: TreeNode, val: int) -> bool:
        if node == None:
            return True
        elif node.val != val:
            return False
        else:
            return (self.isUnivalTreeNode(node.left, val) and self.isUnivalTreeNode(node.right, val))
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return False
        return self.isUnivalTreeNode(root, root.val)
