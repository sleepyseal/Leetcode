class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        return self.merge_sort(head)

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        mid=self.get_mid(head)

        right=self.merge_sort(mid.next)
        mid.next=None
        left=self.merge_sort(head)
        root= self.merge_list(left, right)
        return root
    
    def get_mid(self, head):
        if head is None or head.next is None:
            return head
        slow, fast=head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    
    def merge_list(self, root1, root2):
        dummy_head=ListNode(0)
        cur=dummy_head
        p, q=root1, root2
        while p and q:
            if p.val < q.val:
                cur.next=p
                p=p.next
            else:
                cur.next=q
                q=q.next
            cur=cur.next
        if p:
            cur.next=p
        else:
            cur.next=q
        return dummy_head.next
nums=[-1,5,3,4,0]
root=ListNode(nums[0])
cur=root
for i in range(1, len(nums)):
    new=ListNode(nums[i])
    cur.next=new
    cur=cur.next
print(Solution().sortList(root))