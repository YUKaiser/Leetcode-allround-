# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1!=None:
            curr1=list1
            res=[]
            while curr1.next is not None:
                res.append(curr1.val)
                curr1=curr1.next
            curr1.next=list2
            while curr1 is not None:
                res.append(curr1.val)
                curr1=curr1.next
            res.sort()
            a=0
            curr=list1
            while curr is not None:
                curr.val=res[a]
                a+=1
                curr=curr.next
        head=list1
        if list1==None and list2!=None:
            head=list2
        return head
                
