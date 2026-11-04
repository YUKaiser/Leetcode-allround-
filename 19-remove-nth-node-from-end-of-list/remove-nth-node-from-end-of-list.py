# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is not None:

            cnt=0
            curr=head
            while curr is not None:
                cnt+=1
                curr=curr.next
            if n==cnt:
                head=head.next
                return head
            cnt1=0
            prev=None
            curr1=head
            while curr1 is not None:
                cnt1+=1
                if (cnt-cnt1)+1==n:
                    prev.next=curr1.next
                    break
                prev=curr1
                curr1=curr1.next
        return head
