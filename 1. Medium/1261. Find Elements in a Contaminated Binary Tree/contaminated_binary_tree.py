# Prompt: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
# Runtime: 76 ms, faster than 85.71% of Python online submissions for Find Elements in a Contaminated Binary Tree.
# Memory Usage: 23.7 MB, less than 22.86% of Python online submissions for Find Elements in a Contaminated Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):
    
    def fixNode(self, node):
        """
        :type root: TreeNode
        :rtype: None
        """
        if node.left != None:
            node.left.val = 2 * node.val + 1
            self.val_set.add(node.left.val)
            self.fixNode(node.left)
        if node.right != None:
            node.right.val = 2 * node.val + 2
            self.val_set.add(node.right.val)
            self.fixNode(node.right)

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        root.val = 0
        self.val_set = {0}
        self.root = root
        if root.left != None:
            root.left.val = 1
            self.val_set.add(1)
            self.fixNode(root.left)
        if root.right != None:
            root.right.val = 2
            self.val_set.add(2)
            self.fixNode(root.right)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return (target in self.val_set)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
