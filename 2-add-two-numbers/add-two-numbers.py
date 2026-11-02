# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        elem1=[]
        elem2=[]
        first=l1
        second=l2
        cnt1=0
        cnt2=0
        while first is not None:
            cnt1+=1
            elem1.append(str(first.val))
            first=first.next
        while second is not None:
            cnt2+=1
            elem2.append(str(second.val))
            second=second.next
        elem1.reverse()
        elem2.reverse()
        a="".join(elem1)
        b="".join(elem2)
        c=int(a)+int(b)
        if c==0:
            return ListNode(0)
        res=[]
        while c>0:
            res.append(c%10)
            c=c//10
        
        head=ListNode(res[0])
        curr=head
        for element in res[1:]:
            curr.next=ListNode(element)
            curr=curr.next
        return head