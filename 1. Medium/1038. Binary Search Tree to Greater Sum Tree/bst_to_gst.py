# Prompt: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Runtime: 16 ms, faster than 89.71% of Python online submissions for Binary Search Tree to Greater Sum Tree.
# Memory Usage: 13.6 MB, less than 11.43% of Python online submissions for Binary Search Tree to Greater Sum Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    # populates values list with all vals in tree
    def populateValues(self, node, values):
        """
        :type node: TreeNode
        :type values: List[int]
        :rtype: None
        """
        values.append(node.val)
        if node.left != None:
            self.populateValues(node.left, values)
        if node.right != None:
            self.populateValues(node.right, values)
            
    # sets the values of nodes to their greater sum
    def setNodes(self, node, valToGreaterSum):
        """
        :type node: TreeNode
        :type valToGreaterSum: Dictionary[int, int]
        :rtype: TreeNode
        """
        node.val = valToGreaterSum[node.val]
        
        if node.left != None:
            self.setNodes(node.left, valToGreaterSum)
        if node.right != None:
            self.setNodes(node.right, valToGreaterSum)
    
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        values = []
        self.populateValues(root, values)
        
        # maps values to greater sum for value
        # this works because every value is unique in the BST
        valToGreaterSum = {}
        
        values.sort(reverse=True)
        
        sumSoFar = 0
        for val in values:
            sumSoFar += val
            valToGreaterSum[val] = sumSoFar
            
        self.setNodes(root, valToGreaterSum)
        
        return root
