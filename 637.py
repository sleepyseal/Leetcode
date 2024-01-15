class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return [0]
        q=[root]
        res=[]
        ans=[]
        child=[]
        while q:
            while q:
                ele=q.pop(0)
                ans.append(ele.val)
                if ele.left:
                    child.append(ele.left)
                if ele.right:
                    child.append(ele.right)
            q=child
            child=[]
            res.append(float(sum(ans)/len(ans)))
            ans=[]
        return res
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
l=[3]
t=construct_tree(l)
print(Solution().averageOfLevels(t))
