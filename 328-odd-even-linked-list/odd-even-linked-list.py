# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head!=None:

            curr1=head
            curr2=curr1.next
            evenhead=curr2
            while curr1 is not None and curr2 is not None and curr2.next is not None:
                curr1.next=curr2.next
                curr1=curr1.next
        
                curr2.next=curr1.next
                curr2=curr2.next
            curr1.next=evenhead
        return head

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        