# Prompt: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
# Runtime: 104 ms, faster than 59.34% of Python online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 20.8 MB, less than 90.36% of Python online submissions for Sum of Nodes with Even-Valued Grandparent.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def sumEvenGrandparentRecursive(self, node, evenParent, evenGrandparent):
        """
        :type node: TreeNode
        :type evenParent: bool
        :type evenGrandparent: bool
        :rtype: int
        """

        toReturn = 0
        
        if evenGrandparent:
            toReturn += node.val
        
        if node.left != None:
            toReturn += self.sumEvenGrandparentRecursive(node.left, node.val % 2 == 0, evenParent)
        
        if node.right != None:
            toReturn += self.sumEvenGrandparentRecursive(node.right, node.val % 2 == 0, evenParent)
            
        return toReturn
    
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        toReturn = 0
        if root.left != None:
             toReturn += self.sumEvenGrandparentRecursive(root.left, root.val % 2 == 0, False)
        if root.right != None:
             toReturn += self.sumEvenGrandparentRecursive(root.right, root.val % 2 == 0, False)
                
        return toReturn
