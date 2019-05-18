# Prompt: https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 52 ms, faster than 83.57% of Python3 online submissions for Path Sum.
# Memory Usage: 15.2 MB, less than 46.83% of Python3 online submissions for Path Sum.

class Solution:
    def hasPathSum(self, node: TreeNode, goal: int) -> bool:
        if node == None:
            return False
        if goal == node.val and node.left == None and node.right == None:
            return True
        leftPath = False
        rightPath = False
        if node.left != None:
            leftPath = self.hasPathSum(node.left, goal - node.val)
        if node.right != None:
            rightPath = self.hasPathSum(node.right, goal - node.val)
        return (leftPath or rightPath) # if either path is true
