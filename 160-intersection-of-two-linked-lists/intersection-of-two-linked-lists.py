# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr1=headA
        curr2=headB
        cnt1=0
        cnt2=0
        while curr1 is not None:
            cnt1+=1
            curr1=curr1.next
        while curr2 is not None:
            cnt2+=1
            curr2=curr2.next
        if cnt1>cnt2:
            larger=headA
            smaller=headB

        else:
            larger=headB
            smaller=headA
        skip=abs(cnt1-cnt2)
        for i in range(skip):
            larger=larger.next
        while larger and smaller is not None:
            if larger==smaller:
                return larger
            larger=larger.next
            smaller=smaller.next
        return None
        