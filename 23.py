class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        def merge_list(root1, root2):
            dummy_head=ListNode(0)
            cur=dummy_head
            p, q= root1, root2
            while p and q:
                if p.val<q.val:
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
        child=[]
        while len(lists)>1:
            while lists:
                if len(lists)>1:
                    l1=lists.pop()
                    l2=lists.pop()
                    merged_l=merge_list(l1, l2)
                    child.append(merged_l)
                elif len(lists)==1:
                    child.append(lists.pop())
                else:
                    pass
            lists=child
            child=[]
        return lists[0]
lists = []
lists_node=[]
for i in lists:
    root=ListNode(i[0])
    cur=root
    for j in range(1, len(i)):
        new=ListNode(i[j])
        cur.next=new
        cur=cur.next
    lists_node.append(root)
print(Solution().mergeKLists(lists_node))