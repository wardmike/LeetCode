# Prompt: https://leetcode.com/problems/delete-leaves-with-a-given-value/
# Runtime: 68 ms, faster than 5.06% of Python online submissions for Delete Leaves With a Given Value.
# Memory Usage: 14.4 MB, less than 44.38% of Python online submissions for Delete Leaves With a Given Value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isLeafNode(self, node):
        """
        :type node: TreeNode
        :rtype: bool
        """
        return (node.left == None and node.right == None)
    
    def removeLeafNodesRecursive(self, node, target):
        """
        :type node: TreeNode
        :type target: int
        :rtype: bool
        """
        changed = False
        changedLeft = False
        changedRight = False
        
        if node.left != None:
            # remove node.left if applicable
            if self.isLeafNode(node.left):
                if node.left.val == target:
                    node.left = None
                    changed = True
            else:
                # recursively call node.left
                changedLeft = self.removeLeafNodesRecursive(node.left, target)

        if node.right != None:
            # remove node.right if applicable
            if self.isLeafNode(node.right):
                if node.right.val == target:
                    node.right = None
                    changed = True
            else:
                # recursively call node.right
                changedRight = self.removeLeafNodesRecursive(node.right, target)

        return (changed or changedLeft or changedRight)
    
    
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if self.isLeafNode(root):
                if root.val == target:
                    return None
        
        changed = self.removeLeafNodesRecursive(root, target)
        
        while changed:
            if self.isLeafNode(root):
                if root.val == target:
                    return None
            changed = self.removeLeafNodesRecursive(root, target)
            
        return root
