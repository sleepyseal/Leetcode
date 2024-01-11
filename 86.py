class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
class Solution:
    def partition(self, head, x):
        dummy_head=ListNode(0)
        dummy_head.next=head
        pre=dummy_head
        insert=dummy_head
        cur=head
        while cur:
            if cur.val>=x:
                cur=cur.next
                pre=pre.next
            else:
                if insert==pre:
                    cur=cur.next
                    pre=pre.next
                    insert=insert.next
                else:
                    temp=cur
                    pre.next=cur.next
                    cur=cur.next
                    temp_insert=insert.next
                    insert.next=temp
                    temp.next=temp_insert
                    insert=insert.next
        return dummy_head.next