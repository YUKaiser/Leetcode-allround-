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
        count=0
        curr=head
        while curr is not None:
            count+=1
            curr=curr.next
        
        if count==n:
            return head.next
        
        curr=head
        prev=None
        a=0
        while curr is not None:
            a+=1
            if a==(count-n)+1:
                prev.next=curr.next
                break
            prev=curr
            curr=curr.next
            
        return head
