# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def length(self, head):
        i=0
        cur=head
        while cur:
            i=i+1
            cur=cur.next 
        return i 
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy_head=ListNode(0)
        dummy_head.next=head 
        cur=head 
        l=self.length(cur)
        k=k%l
        tail=head 
        cur=head 
        pre=dummy_head
        while k>1:
            tail=tail.next 
            k-=1
        while tail.next:
            tail=tail.next
            cur=cur.next 
            pre=pre.next
        temp=head 
        dummy_head.next=cur
        tail.next=temp 
        pre.next=None
        return dummy_head.next

        
