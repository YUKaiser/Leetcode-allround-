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
        res=[]
        curr=head
        while curr is not None:
            res.append(curr.val)
            curr=curr.next
        a=res[::-1]
        curr1=head
        k=0
        while curr1 is not None:
            curr1.val=a[k]
            k+=1
            curr1=curr1.next
        return head