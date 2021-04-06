# Prompt: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Runtime: 20 ms, faster than 96.07% of Python online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 18.7 MB, less than 93.01% of Python online submissions for Maximum Difference Between Node and Ancestor.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def maxAncestorDiffRecursive(self, node, minAncestorVal, maxAncestorVal):
        """
        :type node: TreeNode
        :type minAncestorVal: int
        :type maxAncestorVal: int
        :rtype: int
        """
        # returns the max ancestor diff found so far
        
        newMinAncestorVal = minAncestorVal
        newMaxAncestorVal = maxAncestorVal
        
        if node.val < minAncestorVal:
            newMinAncestorVal = node.val
        
        if node.val > maxAncestorVal:
            newMaxAncestorVal = node.val
        
        diffMin = abs(node.val - minAncestorVal)
        diffMax = abs(node.val - maxAncestorVal)
        
        maxSoFar = diffMin if diffMin > diffMax else diffMax
        
        if node.left != None:
            leftDiff = self.maxAncestorDiffRecursive(node.left, newMinAncestorVal, newMaxAncestorVal)
            if leftDiff > maxSoFar:
                maxSoFar = leftDiff
            
        if node.right != None:
            rightDiff = self.maxAncestorDiffRecursive(node.right, newMinAncestorVal, newMaxAncestorVal)
            if rightDiff > maxSoFar:
                maxSoFar = rightDiff
        
        return maxSoFar
    
    
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxAncestorDiffRecursive(root, root.val, root.val)
