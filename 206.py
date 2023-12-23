# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur=head
        pre=None
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre


def init_linked_list(lst):
    if lst is None:
        return None
    
    head=ListNode(lst[0])
    cur=head
    for i in lst:
        cur.next=ListNode(i)
        cur=cur.next
    return head
