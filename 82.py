class ListNode:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

class Solution:
    # def deleteDuplicates(self, head):
    #     dic_h={}
    #     cur=head
    #     dummy_head=ListNode(0)
    #     dummy_head.next=head
    #     pre=dummy_head
    #     while cur:
    #         if cur.val not in dic_h:
    #             dic_h[cur.val]=1
    #             cur=cur.next
    #         else:
    #             dic_h[cur.val]+=1
    #             cur=cur.next
    #     cur=head
    #     while cur:
    #         if dic_h[cur.val]==1:
    #             cur=cur.next
    #             pre=pre.next
    #         else:
    #             while cur.next:
    #                 cur=cur.next
    #                 if dic_h[cur.val]==1:
    #                     break
    #             if cur.next is None:
    #                 if dic_h[cur.val]==1:
    #                     pre.next=cur
    #                 else:
    #                     pre.next=None
    #                 cur=cur.next
    #             else:
    #                 pre.next=cur
    #                 pre=pre.next
    #                 cur=cur.next

    #     return dummy_head.next
    def deleteDuplicates(self, head):
        dummy_head=ListNode(0)
        dummy_head.next=head
        pre=dummy_head
        cur=head
        while cur and cur.next:
            if cur.val!=cur.next.val:
                pre=pre.next
                cur=cur.next
            else:
                val=cur.val
                while cur.next and cur.next.val==val:
                    cur=cur.next
                pre.next=cur.next
                cur=pre.next
        return dummy_head.next
            
l=[1,2,3,3,4,4,5]
head=ListNode(l[0])
cur=head
for i in l[1:]:
    new=ListNode(i)
    cur.next=new
    cur=cur.next
print(Solution().deleteDuplicates(head))