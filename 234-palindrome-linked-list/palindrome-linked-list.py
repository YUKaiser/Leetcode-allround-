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
        arr=[]
        curr=head
        while curr is not None:
            arr.append(curr.val)
            curr=curr.next

        if arr[::-1]==arr:
            return True
        return False
          
        