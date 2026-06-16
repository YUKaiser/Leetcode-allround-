# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next

        prev=None
        curr=head
        while curr is not None:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return head
       
    
    
        