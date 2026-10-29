# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        
        prev=None
        curr=node
        while curr.next is not None:
            prev=curr
            curr=curr.next
            prev.val=curr.val
        prev.next=None

        
        