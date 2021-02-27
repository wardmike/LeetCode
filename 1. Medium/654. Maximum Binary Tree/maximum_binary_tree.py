# Prompt: https://leetcode.com/problems/maximum-binary-tree/
# Runtime: 208 ms, faster than 50.92% of Python online submissions for Maximum Binary Tree.
# Memory Usage: 14.1 MB, less than 54.35% of Python online submissions for Maximum Binary Tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if len(nums) == 0:
            return None
        
        maxVal = 0
        maxIndex = 0
        
        for i, n in enumerate(nums):
            if n > maxVal:
                maxVal = n
                maxIndex = i
                
        node = TreeNode(maxVal)
        
        node.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        node.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        
        return node
