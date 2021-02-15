# Prompt: https://leetcode.com/problems/add-two-numbers-ii/
# Runtime: 72 ms, faster than 31.76% of Python online submissions for Add Two Numbers II.
# Memory Usage: 13.7 MB, less than 21.50% of Python online submissions for Add Two Numbers II.


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
        
        if l1 == None or l2 == None:
            return ListNode()
        
        # turn both linked lists into integers
        l1Val = int(l1.val)
        l2Val = int(l2.val)
        
        while l1.next != None:
            l1 = l1.next
            l1Val *= 10
            l1Val += int(l1.val)
            
        while l2.next != None:
            l2 = l2.next
            l2Val *= 10
            l2Val += int(l2.val)
            
        # add together
        sumVals = l1Val + l2Val
        
        # turn sum into linked list
        digits = len(str(sumVals))
        
        sumL = ListNode()
        current = sumL
        while digits > 0:
            val = sumVals / 10 ** (digits - 1)
            sumVals -= val * 10 ** (digits - 1)
            digits -= 1

            current.val = val
            if digits > 0:
                current.next = ListNode()
                current = current.next
                
        return sumL
