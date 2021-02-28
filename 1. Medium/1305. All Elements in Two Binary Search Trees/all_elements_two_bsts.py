# Prompt: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Runtime: 944 ms, faster than 5.67% of Python online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 22.5 MB, less than 46.45% of Python online submissions for All Elements in Two Binary Search Trees.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def treeToList(self, node):
        """
        :type node: TreeNode
        :rtype: List[int]
        """
        if node == None:
            return []
            
        if node.left == None and node.right == None:
            return [node.val]
        
        left = []
        if node.left != None:
            left = self.treeToList(node.left)
        right = []
        if node.right != None:
            right = self.treeToList(node.right)
        
        return left + right + [node.val]
    
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        return sorted(self.treeToList(root1) + self.treeToList(root2))
