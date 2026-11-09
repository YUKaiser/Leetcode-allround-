# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        rs=[]
        curr=head
        while curr is not None:
            rs.append(curr.val)
            curr=curr.next
        a=0
        b=len(rs)-1
        while a<b:
            if rs[a]!=rs[b]:
                return False
            a+=1
            b-=1
        return True
        