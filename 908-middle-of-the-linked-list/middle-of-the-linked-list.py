# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count=0
        curr=head
        while curr is not None:
            count+=1
            curr=curr.next
        
        curr1=head
        trav=count//2
        i=0
        while i<trav:
            curr1=curr1.next
            i+=1
        return curr1