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
        curr1=l1
        curr2=l2
        carry=0
        count1=0
        count2=0
        while curr1 is not None:
            count1+=1
            curr1=curr1.next
        while curr2 is not None:
            count2+=1
            curr2=curr2.next
        curr1=l1
        curr2=l2
        if count1>=count2:
            a=curr1
            b=curr2     
        else:
            a=curr2
            b=curr1
        head=a
        while a is not None and b is not None:
            a.val+=b.val+carry
            if a.val >=10:
                carry=1
                a.val=a.val-10
            else:
                carry=0
            prev=a
            a=a.next
            b=b.next

        while carry!=0 and a is not None:
            a.val+=carry
            if a.val==10:
                carry=1
                a.val=0
            else:
                carry=0
            prev=a
            a=a.next
        
        if carry!=0:
            prev.next=ListNode(1)

    

        return head