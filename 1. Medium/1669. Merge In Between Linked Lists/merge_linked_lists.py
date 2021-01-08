# Prompt: https://leetcode.com/problems/merge-in-between-linked-lists/
# Runtime: 1040 ms, faster than 5.28% of Python online submissions for Merge In Between Linked Lists.
# Memory Usage: 30.5 MB, less than 5.87% of Python online submissions for Merge In Between Linked Lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    # find the node with specific position within a linked list
    def findNode(self, node, pos):
        """
        :type node: ListNode
        :type pos: int
        :rtype: ListNode
        """
        if pos == 0:
            return node
        else:
            return self.findNode(node.next, pos-1)
        
    # find last node in a linked list
    def findLast(self, node):
        """
        :type node: ListNode
        :rtype: ListNode
        """
        if node.next == None:
            return node
        else:
            return self.findLast(node.next)
    
    # delete all nodes in a linked list
    def deleteList(self, node):
        """
        :type node: ListNode
        :rtype: None
        """
        while node.next != None:
            prev = node
            node = node.next
            del(prev)

    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # find important nodes
        A = self.findNode(list1, a)
        beforeA = self.findNode(list1, a-1)
        afterB = self.findNode(list1, b+1)
        endOfList2 = self.findLast(list2)
        
        # point a-1 to list2
        beforeA.next = list2
        
        # point end of list 2 to b+1
        endOfList2.next = afterB
        
        # delete unused part
        self.deleteList(A)
        
        return list1
