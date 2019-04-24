# Prompt: https://leetcode.com/problems/leaf-similar-trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Runtime: 40 ms, faster than 73.89% of Python3 online submissions for Leaf-Similar Trees.
# Memory Usage: 13.1 MB, less than 5.32% of Python3 online submissions for Leaf-Similar Trees.
class Solution:
    # dfs (left to right) adding all leaf nodes to list
    def dfs(self, node: TreeNode) -> List[int]:
        l = []
        if node.left == None and node.right == None: # leaf node
            l.append(node.val)
        else:
            if node.left != None: # call left first to ensure left-to-right
                l.extend(self.dfs(node.left))
            if node.right != None:
                l.extend(self.dfs(node.right))
        return l

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # bfs result will be the same iff trees are leaf similar
        return (self.dfs(root1) == self.dfs(root2))
