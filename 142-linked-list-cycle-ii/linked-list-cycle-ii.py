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
        curr=head
        s_s=set()
        while curr is not None and curr.next is not None:
            if curr in s_s:
                return curr
            s_s.add(curr)
            curr=curr.next
        return None
