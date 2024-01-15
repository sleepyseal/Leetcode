class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next=next
class Solution:
    def connect(self, root):
        if root is None:
            return None
        q=[root]
        while q:
            head=q[0]
            for i in q[1:]:
                if i:
                    head.next=i
                    head=i
            child=[]
            while q:
                ele=q.pop(0)
                if ele and ele.left:
                    child.append(ele.left)
                if ele and ele.right:
                    child.append(ele.right)
            q=child
        return root
root = [1,2,3,4,5,None,7]
def construct_tree(lst):
    if lst is None:
        return
    head=TreeNode(lst[0])
    queue=[]
    queue.append(head)
    i=0
    while i<len(lst):
        ele=queue.pop(0)
        i=i+1
        if i<len(lst) and lst[i] is not None:
            new=TreeNode(lst[i])
            queue.append(new)
            ele.left=new
        i=i+1
        if i<len(lst) and lst[i] is not None:
            new=TreeNode(lst[i])
            queue.append(new)
            ele.right=new
    return head
t=construct_tree(root)
print(Solution().connect(t))