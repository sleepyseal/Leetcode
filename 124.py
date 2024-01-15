class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        if root is None:
            return 0
        ans=[-1000]
        def dfs(root, ans):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                if root.val>ans[0]:
                    ans[0]=root.val
                return root.val
            if root.val>ans[0]:
                ans[0]=root.val
            left=dfs(root.left, ans)
            right=dfs(root.right, ans)
            if max(left, 0)+max(right, 0)+root.val>ans[0]:
                ans[0]=max(left, 0)+max(right, 0)+root.val
            return max(max(0, left), max(0, right))+root.val
        dfs(root, ans)
        return ans[0]
root = [0]
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
l=construct_tree(root)
print(Solution().maxPathSum(l))