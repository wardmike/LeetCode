# Prompt: https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        count = 0
        # find total number of nodes
        while (node.next != None):
            node = node.next
            count += 1
        # find index of middle node
        index = 0
        if count % 2 == 0:
            index = count / 2
        else:
            index= count / 2 + 1
        node = head
        # get middle node
        for i in range(int(index)):
            node = node.next
        return node
