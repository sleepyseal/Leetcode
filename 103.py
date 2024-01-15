class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        flag=1
        q=[root]
        child=[]
        ans=[]
        while q:
            cur_val=[]
            while q:
                ele=q.pop(0)
                cur_val.append(ele.val)
                if ele.left:
                    child.append(ele.left)
                if ele.right:
                    child.append(ele.right)
            if flag==1:
                ans.append(cur_val)
            else:
                cur_val.reverse()
                ans.append(cur_val)
            q=child
            child=[]
            flag=-1*flag
        return ans
def construct_tree(l):
    root=TreeNode(l[0])
    q=[root]
    i=1
    while i<len(l):
        ele=q.pop(0)
        if i<len(l) and i !=None:
            new=TreeNode(l[i])
            q.append(new)
            ele.left=new
        i+=1
        if i<len(l) and i !=None:
            new=TreeNode(l[i])
            q.append(new)
            ele.right=new
        i+=1
    return root
l=[1,2,3,4,None,None,5]
t=construct_tree(l)
print(Solution().zigzagLevelOrder(t))
