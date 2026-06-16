class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count=0 #to count the number of nodes in the linked list
        curr=head  #to traverse the linked list
        while curr is not None:
            count+=1
            curr=curr.next
        
        curr1=head #to traverse the linked list again to reach the middle node
        trav=count//2 #to calculate the number of nodes to traverse to reach the middle node
        i=0
        while i<trav: #to traverse the linked list until we reach the middle node
            curr1=curr1.next
            i+=1
        return curr1 #to return the middle node of the linked list