class Solution:
    def isValidBST(self, root):
        # pre=-float('inf')
        # p=root
        # stack=[]
        # while p or stack:
        #     while p:
        #         stack.append(p)
        #         p=p.left
        #     p=stack.pop()
        #     if p.val<=pre:
        #         return False
        #     pre=p.val
        #     p=p.right
        # return True
        def dfs(root, pre, ans):
            if root is None:
                return
            dfs(root.left, pre, ans)
            if pre[0]>=root.val:
                ans[0]=False
            pre[0]=root.val
            dfs(root.right, pre, ans)
        pre=[-100000]
        ans=[True]
        dfs(root, pre, ans)
        return ans[0]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def construct_tree(l):
    root=TreeNode(l[0])
    q=[root]
    i=1
    while i<len(l):
        ele=q.pop(0)
        if i<len(l) and l[i]!=None:
            new=TreeNode(l[i])
            q.append(new)
            ele.left=new
        i+=1
        if i<len(l) and l[i]!=None:
            new=TreeNode(l[i])
            q.append(new)
            ele.right=new
        i+=1
    return root

l=[5,1,4,None,None,3,6]
t=construct_tree(l)
print(Solution().isValidBST(t))