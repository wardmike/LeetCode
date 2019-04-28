# Prompt: https://leetcode.com/problems/trim-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 60 ms, faster than 77.33% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 17.4 MB, less than 5.36% of Python3 online submissions for Trim a Binary Search Tree.

class Solution:
    def findNodesWithinRange(self, node: TreeNode, L: int, R: int, toKeep: List[int]) -> None:
        if node != None:
            if node.val >= L and node.val <= R:
                toKeep.append(node.val)
                self.findNodesWithinRange(node.left, L, R, toKeep)
                self.findNodesWithinRange(node.right, L, R, toKeep)
            elif node.val > R:
                self.findNodesWithinRange(node.left, L, R, toKeep)
            elif node.val < L:
                self.findNodesWithinRange(node.right, L, R, toKeep)
                
    def addNode(self, node: TreeNode, val: int):
        if node.val > val:
            if node.left == None:
                node.left = TreeNode(val)
            else:
                self.addNode(node.left, val)
        else:
            if node.right == None:
                node.right = TreeNode(val)
            else:
                self.addNode(node.right, val)
            
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        # to keep
        toKeep = []
        self.findNodesWithinRange(root, L, R, toKeep)
        if len(toKeep) > 0:
            i = 0
            newTree = TreeNode(toKeep[i])
            i += 1
            while i < len(toKeep):
                self.addNode(newTree, toKeep[i])
                i += 1
            return newTree
        return []
