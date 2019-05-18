# Prompt: https://leetcode.com/problems/count-univalue-subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
 Notes:
 Bottom-up recursive solution that finds number of unival sub-trees & then finds if current node is
 part of a unival subtree. Challenge is to keep track of whether we have a possible unival sub-tree
 while we go up and also keeping track of count of unival subtrees. One solution is to return a bool
 for possible unival sub-tree & keep track of count in a class-level var, but this solution returns
 both as a list.
"""

# Runtime: 40 ms, faster than 97.37% of Python3 online submissions for Count Univalue Subtrees.
# Memory Usage: 13.2 MB, less than 54.70% of Python3 online submissions for Count Univalue Subtrees.

class Solution:
    # bottom-up recursion
    # returned list has two elems: first is for the number of unival trees so far, second is
    # a bool representing if this side is all unival (possibly part of a bigger unival)
    def countUnival(self, node: TreeNode) -> List[int]:
        # base case - null node (0 unival trees but possible part of bigger unival)
        if node == None:
            return [0, True]
        
        # setting default if child ptr is null - possible unival is true b/c null sides don't prevent unival
        leftSide = [0, True]
        rightSide = [0, True]
        
        # find left sub-tree
        if node.left != None:
            leftSide = self.countUnival(node.left)
            
        # find right sub-tree
        if node.right != None:
            rightSide = self.countUnival(node.right)
        
        # are both subtrees possible unival?
        if leftSide[1] and rightSide[1]:
            
            # all existing children must equal parent (leaf nodes are unival)
            if (node.left == None or node.val == node.left.val) and (node.right == None or node.val == node.right.val):
                return [leftSide[0] + rightSide[0] + 1, True]
        
        # else case - this subtree is not unival
        return [leftSide[0] + rightSide[0], False]        
        
        
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        # return only the int from list
        return self.countUnival(root)[0]
