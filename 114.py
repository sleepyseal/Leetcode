class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root):
        if root is None :
            return root       
        right=root.right
        root.right=self.flatten(root.left)
        root.left=None
        cur=root
        while cur.right:
            cur=cur.right
        cur.right=self.flatten(right)

        return root
root = [1,2,5,3,4,None,6]

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
ans=Solution().flatten(t)
print('')