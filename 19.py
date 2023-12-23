class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head=ListNode(0)
        dummy_head.next=head
        pre=dummy_head
        cur=head 
        if cur is None or cur.next is None:
            return dummy_head
        i=1
        while i<n:
            cur=cur.next
            i=i+1
        while cur.next is not None:
            pre=pre.next 
            cur=cur.next 
        pre.next=pre.next.next 
        return dummy_head.next