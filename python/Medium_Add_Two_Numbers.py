# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def checkOne(self, l):
        """
        :type l: ListNode
        :rtype: ListNode
        """
        val = (l.val) % 10
        tens = int ((l.val) / 10)
        result = ListNode(val)
        result.next = (l.next)
        if result.next:
            result.next.val += tens
        elif tens > 0:
            result.next = ListNode(tens)
        return result
    
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            val = (l1.val + l2.val) % 10
            tens = int ((l1.val + l2.val) / 10)
            result = ListNode(val)
            if l1.next:
                l1.next.val += tens
            elif tens > 0:
                l1.next = ListNode(tens)
            result.next = self.addTwoNumbers(l1.next,l2.next)
        elif l1 or l2:
            result = self.checkOne(l1 or l2)
            result.next = self.addTwoNumbers(result.next,None)
        else:
            result = None
        return result
