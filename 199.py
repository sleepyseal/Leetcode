class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        ans=[root.val]
        q=[root]
        child=[]
        while q:
            while q:
                ele=q.pop(0)
                if ele.left:
                    child.append(ele.left)
                if ele.right:
                    child.append(ele.right)
            q=child
            if child:
                ans.append(child[-1].val)
            child=[]
        return ans
def construct_tree(l):
    root=TreeNode(l[0])
    q=[root]
    i=1
    ele=q.pop(0)
    while i<len(l):
        if l[i] is None:
            ele.left= None
        else:
            new=TreeNode(l[i])
            ele.left=new
            q.append(new)
        i+=1
        if l[i] is None:
            ele.right=None
        else:
            new=TreeNode(l[i])
            ele.right=new
            q.append(new)
        i+=1
        ele=q.pop(0)
