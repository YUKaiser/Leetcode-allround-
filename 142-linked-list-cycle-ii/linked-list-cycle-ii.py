# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if  fast==slow:
                break
        slow=head
        while fast is not None and fast.next is not None:
            if slow==fast:
                return slow
            fast=fast.next
            slow=slow.next
        return None
        