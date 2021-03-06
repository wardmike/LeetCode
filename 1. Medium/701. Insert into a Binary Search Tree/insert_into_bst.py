# Prompt: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Runtime: 132 ms, faster than 60.25% of Python online submissions for Insert into a Binary Search Tree.
# Memory Usage: 17.4 MB, less than 95.50% of Python online submissions for Insert into a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        if root == None:
            return TreeNode(val)
        
        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        else:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)

        return root
