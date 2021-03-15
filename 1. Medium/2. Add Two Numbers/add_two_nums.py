# Prompt: https://leetcode.com/problems/add-two-numbers/
# Runtime: 60 ms, faster than 68.48% of Python online submissions for Add Two Numbers.
# Memory Usage: 13.6 MB, less than 17.61% of Python online submissions for Add Two Numbers.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        val = l1.val + l2.val
        remainder = 0
        if val > 9:
            val -= 10
            remainder = 1
        root = ListNode(val)
        temp = root
        
        
        while l1.next != None or l2.next != None:
            if l1.next != None:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = 0
            
            val = l1.val + l2.val + remainder
            remainder = 0
            if val > 9:
                val -= 10
                remainder = 1
            temp.next = ListNode(val)
            
            temp = temp.next
            
        if remainder > 0:
            temp.next = ListNode(remainder)
            
        return root
