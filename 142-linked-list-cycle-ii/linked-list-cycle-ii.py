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
        dic={}
        while curr is not None and curr.next is not None:
            if curr in dic:
                return curr
            dic[curr]=dic.get(curr.val)
            curr=curr.next
        return None
