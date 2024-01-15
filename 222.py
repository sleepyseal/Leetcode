class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        h=0
        head=root
        while head:
            h+=1
            head=head.left
        ans=[0]
        def dfs(root,height, h, ans):
            if root.left is None and root.right is None and height==h:
                return
            if root.left is not None and root.right is None and height==h-1:
                ans[0]+=1
            elif root.left is None and root.right is None and height==h-1:
                ans[0]+=2
            else:
                height+=1
                if root.left is not None and root.right is not None and height==h:
                    return
                else:
                    dfs(root.right, height, h, ans)
                    dfs(root.left, height, h, ans)
        dfs(root, 1, h, ans)
        return pow(2, h)-ans[0]-1

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
root = [1,2,3,4,5,6,7,8]
l=construct_tree(root)
print(Solution().countNodes(l))
