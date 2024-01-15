class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root):
        if root is None:
            return 0
        ans=[]
        def num_str(root, s, ans):
            if root.left is None and root.right is None:
                ans.append(s+str(root.val))
                return
            s=s+str(root.val)
            if root.left:
                num_str(root.left, s, ans)
            if root.right:
                num_str(root.right, s, ans)
        num_str(root, '', ans)
        res=0
        for i in ans:
            res+=int(i)
        return res
root = [4,9,0,5,1]
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
print(Solution().sumNumbers(t))