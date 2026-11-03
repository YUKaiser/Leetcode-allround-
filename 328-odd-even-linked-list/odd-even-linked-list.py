# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        lis=[]
        while curr is not None:
            lis.append(curr.val)
            curr=curr.next
        seq=[]
        a=0
        while a<len(lis):
            seq.append(lis[a])
            a+=2
        b=1
        while b<len(lis):
            seq.append(lis[b])
            b+=2
        c=0
        curr2=head
        while curr2 is not None:
            curr2.val=seq[c]
            c+=1
            curr2=curr2.next
        
        return head
