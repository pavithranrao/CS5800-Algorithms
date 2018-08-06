# Definition for singly-linked list.
# class ListNode(object):
#     def _init_(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head:
            cur = head
            count = 1
            while cur.next:
                count += 1
                cur = cur.next
            shift = count - (k % count)
            if shift:
                cur.next = head
                idx = 0
                while idx < shift:
                    cur = cur.next
                    idx += 1
                tmp = cur.next
                cur.next = None
                return tmp
            else:
                return head
        else:
            return None

