# Prompt: https://leetcode.com/problems/n-ary-tree-preorder-traversa
"""
 Notes:
 # Definition for a Node.
 class Node:
     def __init__(self, val, children):
         self.val = val
         self.children = children #list of nodes
"""
# Runtime: 96 ms, faster than 74.88% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 17.6 MB, less than 5.26% of Python3 online submissions for N-ary Tree Preorder Traversal.
class Solution:
    def preorderNode(self, node: 'Node', traversal: List[int]) -> None:
        if node != None:
            traversal.append(node.val)
            for child in node.children:
                self.preorderNode(child, traversal)
    def preorder(self, root: 'Node') -> List[int]:
        traversal = []
        self.preorderNode(root, traversal)
        return traversal
