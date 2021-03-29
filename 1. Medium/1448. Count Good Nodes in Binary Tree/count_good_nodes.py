# Prompt: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Runtime: 292 ms, faster than 68.29% of Python online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 49.3 MB, less than 71.36% of Python online submissions for Count Good Nodes in Binary Tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def goodNodes(self, node, maxParent=0-10**4):
        """
        :type node: TreeNode
        :type maxParent: int
        :rtype: int
        """
        if node == None:
            return 0
        
        newMaxParent = maxParent
        good = 0
        if node.val >= maxParent:
            newMaxParent = node.val
            good += 1 # for this node
            
        if node.left != None:
            good += self.goodNodes(node.left, newMaxParent)
        
        if node.right != None:
            good += self.goodNodes(node.right, newMaxParent)
               
        return good
