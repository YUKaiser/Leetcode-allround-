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
        dicta={}
        curr=head
        while curr is not None:
            if curr in dicta.values():
                return curr
            dicta[curr]=curr
            curr=curr.next
        return None
        