# Prompt: https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 256 ms, faster than 53.81% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 21.8 MB, less than 5.06% of Python3 online submissions for Range Sum of BST.

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None: # node here doesn't exist
            return 0
        elif root.val >= L and root.val <= R: # val is in range; add it & call both left and right
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        elif root.val < L: # we're too small; call only right
            return self.rangeSumBST(root.right, L, R)
        else: # we're too big; call only left
            return self.rangeSumBST(root.left, L, R)
        
