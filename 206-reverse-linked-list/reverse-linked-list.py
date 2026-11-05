# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a=None
        b=head
        while b is not None:
            vara=b
            varb=b.next
            b.next=a
            a=vara
            b=varb
        head=b
        return a