# Prompt: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
 Notes: same as 589. preorder traversal, except that node.val is added
 after children.
 # Definition for a Node.
 class Node:
     def __init__(self, val, children):
         self.val = val
         self.children = children #list of nodes
"""
# Runtime: 116 ms, faster than 16.69% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 17.6 MB, less than 6.03% of Python3 online submissions for N-ary Tree Postorder Traversal.
class Solution:
    def postorderNode(self, node: 'Node', traversal: List[int]) -> None:
        if node != None:
            for child in node.children:
                self.postorderNode(child, traversal)
            traversal.append(node.val)
    def postorder(self, root: 'Node') -> List[int]:
        traversal = []
        self.postorderNode(root, traversal)
        return traversal
        
