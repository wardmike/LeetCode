# Prompt: https://leetcode.com/problems/deepest-leaves-sum/
# Runtime: 108 ms, faster than 30.33% of Python online submissions for Deepest Leaves Sum.
# Memory Usage: 20.9 MB, less than 82.33% of Python online submissions for Deepest Leaves Sum.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.valPerDepth = {}
        
    # populates self.valPerDepth
    def deepestLeavesSumRecursive(self, node, depth):
        """
        :type node: TreeNode
        :type depth: int
        :rtype: None
        """
        if node != None:
            if depth in self.valPerDepth:
                self.valPerDepth[depth] += node.val
            else:
                self.valPerDepth[depth] = node.val
        if node.left != None:
            self.deepestLeavesSumRecursive(node.left, depth+1)
        if node.right != None:
            self.deepestLeavesSumRecursive(node.right, depth+1)

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.deepestLeavesSumRecursive(root, 0)
        
        deepest = 0
        for depth in self.valPerDepth:
            if depth > deepest:
                deepest = depth
                
        return self.valPerDepth[deepest]
