# Prompt: https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 48 ms, faster than 88.80% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.9 MB, less than 5.13% of Python3 online submissions for Maximum Depth of Binary Tree.

class Solution:
    # maxSoFar is a list w/ 1 element so that it is passed by reference
    def maxDepthRecursive(self, node: TreeNode, currentDepth: int, maxSoFar: List[int]) -> None:
        if currentDepth > maxSoFar[0]:
            maxSoFar[0] = currentDepth
        if node.left != None:
            self.maxDepthRecursive(node.left, currentDepth + 1, maxSoFar)
        if node.right != None:
            self.maxDepthRecursive(node.right, currentDepth + 1, maxSoFar)
    
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        maxSoFar = [1]
        self.maxDepthRecursive(root, 1, maxSoFar)
        return maxSoFar[0]
