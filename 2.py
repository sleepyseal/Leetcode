# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1=l1
        p2=l2
        dummy_head=ListNode(0)
        cur=dummy_head
        add_front=0
        while p1 is not None and p2 is not None:
            if add_front>0:
                val=p1.val+p2.val+1
                add_front=add_front-1
            else:
                val=p1.val+p2.val
            if val >9:
                val=val-10
                add_front=1
            cur.next=ListNode(val)
            cur=cur.next 
            p1=p1.next 
            p2=p2.next 
        while p1 is not None:
            if add_front>0:
                val=p1.val+1
                add_front=-1
            else:
                val=p1.val 
            if val >9:
                val=val-10
                add_front=1
            cur.next=ListNode(val)
            cur=cur.next 
            p1=p1.next
        while p2 is not None:
            if add_front>0:
                val=p2.val+1
                add_front=-1
            else:
                val=p2.val 
            if val >9:
                val=val-10
                add_front=1
            cur.next=ListNode(val)
            cur=cur.next 
            p2=p2.next 
        if add_front==1:
            cur.next=ListNode(1)
            cur=cur.next 
        return dummy_head.next 
    
def init_linked_list(lst):
    if not lst:  # 空列表情况
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
l1=init_linked_list([2,4,3])
l2=init_linked_list([5,6,4])
s=Solution()
s.addTwoNumbers(l1, l2)
