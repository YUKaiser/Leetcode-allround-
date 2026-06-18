class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr=head
        dic={}
        count=0
        while curr is not None and curr.next!=None:
            if curr not in dic:
                dic[curr]=dic.get(curr.val)
            else:
                return True
            curr=curr.next
        return False