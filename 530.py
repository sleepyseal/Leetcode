class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root):
        # p=root
        # stack=[]
        # pre=-1000000
        # ans=10000000
        # while p is not None or stack:
        #     while p is not None:
        #         stack.append(p)
        #         p=p.left
        #     p=stack.pop()
        #     cur_val=p.val
        #     if cur_val-pre<ans:
        #         ans=cur_val-pre
        #     pre=cur_val
        #     p=p.right

        # return ans
        def dfs(root, pre, ans):
            if root is None:
                return
            dfs(root.left, pre, ans)
            ans[0]=min(root.val-pre[0], ans[0])
            pre[0]=root.val
            dfs(root.right, pre, ans)
        pre=[-1000000]
        ans=[1000000]
        dfs(root, pre, ans)
        return ans[0]
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
l=[600,424,612,None,499,None,689]
t=construct_tree(l)
Solution().getMinimumDifference(t)