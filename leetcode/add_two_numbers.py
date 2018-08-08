# Definition for singly-linked list.
# class ListNode(object):
#     def _init_(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(None)
        cur = result
        
        while l1 or l2:
            if l1 and l2:
                sum_of_digits = l1.val + l2.val + carry
            else:
                sum_of_digits = (l1 or l2).val + carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur.next = ListNode(sum_of_digits % 10)
            carry = sum_of_digits / 10
            cur = cur.next
            
        
        if carry:
            cur.next = ListNode(carry)
            
        
        return result.next
