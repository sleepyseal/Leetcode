class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root):
        ans=100000
        def dfs(root, ans):
            if root is None:
                return
            if root.left is None and root.right is None:
                return root.val
            left, right=-100000, 100000
            if root.left:
                left= dfs(root.left, ans)
            cur_val=root.val
            if cur_val-left<ans:
                ans=cur_val-left
            if root.right:
                right= dfs(root.right, ans)
            if right- cur_val<ans:
                ans=right-cur_val
            return cur_val
        dfs(root, ans)
        return ans
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