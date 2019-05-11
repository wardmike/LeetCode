# Prompt: https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 32 ms, faster than 99.23% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.3 MB, less than 5.74% of Python3 online submissions for Invert Binary Tree.

class Solution:
    def invertTreeRecursive(self, node: TreeNode) -> None:
        temp = node.left
        node.left = node.right
        node.right = temp
        if node.left != None:
            self.invertTreeRecursive(node.left)
        if node.right != None:
            self.invertTreeRecursive(node.right)
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root != None:
            self.invertTreeRecursive(root)
        return root
