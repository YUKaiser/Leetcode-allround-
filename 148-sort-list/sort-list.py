# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        lis=[]
        curr=head
        while curr is not None:
            lis.append(curr)
            curr=curr.next
        lis.sort(key=lambda x:x.val)
        for i in range(len(lis)-1):
            lis[i].next=lis[i+1]
        lis[-1].next=None
        return lis[0]
