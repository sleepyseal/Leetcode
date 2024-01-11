class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
    
class Solution:
    def reverseKGroup(self, head, k):
        dummy_head=ListNode(0)
        dummy_head.next=head
        pre=dummy_head
        cur=head
        def reverse_list(first, tail):
            cur=first.next.next
            pre=first.next
            while cur !=tail:
                temp=cur
                pre.next=cur.next
                first_post=first.next
                first.next=temp
                temp.next=first_post
                cur=pre.next
            return pre
                
        l=1
        while cur.next:
            if l<k:
                cur=cur.next
                l+=1
            else:
                pre=reverse_list(pre, cur.next)
                cur=pre.next
                l=1
        if l==k:
            reverse_list(pre, None)
        return dummy_head.next

head = [1,2,3,4,5]
k=3
l=ListNode(head[0])
cur=l
for i in head[1:]:
    new=ListNode(i)
    cur.next=new
    cur=cur.next
print(Solution().reverseKGroup(l, k))