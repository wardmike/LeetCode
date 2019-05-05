# Prompt: https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 100 ms, faster than 48.81% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 15.4 MB, less than 5.00% of Python3 online submissions for Two Sum IV - Input is a BST.

class Solution:
    # modifies sortedList in place
    def buildListRecursive(self, node: TreeNode, sortedList: List[int]) -> None:
        if node != None:
            self.buildListRecursive(node.left, sortedList)
            sortedList.append(node.val)
            self.buildListRecursive(node.right, sortedList)
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        sortedList = []
        self.buildListRecursive(root, sortedList)
        # two-pointer method
        lower = 0
        upper = len(sortedList) - 1
        while lower < upper:
            pair = sortedList[lower] + sortedList[upper]
            if pair == k:
                return True
            elif pair < k:
                lower += 1
            else:
                upper -= 1
        return False
        
