# Prompt: https://leetcode.com/problems/merge-two-binary-trees
"""
Notes:
 Definition for a binary tree node.
  class TreeNode:
      def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None
"""
# Runtime: 112 ms, faster than 11.37% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 14.6 MB, less than 5.13% of Python3 online submissions for Merge Two Binary Trees.
class Solution:
    def mergeTrees(self, t1, t2):
        t3 = TreeNode(0)
        if t1 == None and t2 == None:
            return None
        elif t1 != None and t2 != None:
            t3.val = t1.val + t2.val
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
        elif t1 == None:
            t3.val = t2.val
            t3.left = self.mergeTrees(None, t2.left)
            t3.right = self.mergeTrees(None, t2.right)
        elif t2 == None:
            t3.val = t1.val
            t3.left = self.mergeTrees(t1.left, None)
            t3.right = self.mergeTrees(t1.right, None)
        return t3
