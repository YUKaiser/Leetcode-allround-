class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 1. slow and fast pointer(tortoise and hare)
        # -here what we are doing is we are moving the fast pointer twice as fast as the slow pointer,
        #  so when the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list.)
        slow=fast=head  
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow