# Prompt: https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 56 ms, faster than 22.97% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.6 MB, less than 26.81% of Python3 online submissions for Maximum Depth of Binary Tree.

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        leftDepth = 0
        rightDepth = 0
        if root.left != None:
            leftDepth = self.maxDepth(root.left)
        if root.right != None:
            rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1
