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
        countA=0
        countB=0
        currA=headA
        while currA is not None:
            countA+=1
            currA=currA.next
        currB=headB
        while currB is not None:
            countB+=1
            currB=currB.next
        
        currA=headA
        currB=headB

        if countA>countB:
            a=0
            while a<(countA-countB):
                currA=currA.next
                a+=1
        else:
            a=0
            while a <(countB-countA):
                currB=currB.next
                a+=1
        while currA is not None and currB is not None:
            if currA==currB:
                return currA
            currA=currA.next
            currB=currB.next
        return None