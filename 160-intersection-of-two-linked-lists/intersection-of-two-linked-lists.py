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
        if headA is None or headB is None:
            return None
        currA=headA
        set_=set()
        while currA is not None:
            set_.add(currA)
            currA=currA.next
        currB=headB
        while currB is not None:
            if currB in set_:
                return currB
            currB=currB.next
        
        return None
        