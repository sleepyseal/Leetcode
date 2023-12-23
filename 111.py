class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.right is None and root.left is not None:
            return 1+self.minDepth(root.left)
        elif root.right is not None and root.left is None:
            return 1+self.minDepth(root.right)
        elif root.right is None and root.left is None:
            return 1
        else:
            left_dp=0
            right_dp=0
            left_dp=self.minDepth(root.left)
            right_dp=self.minDepth(root.right)
            return min(right_dp, left_dp)+1
        
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
l=[3,9,20,None,None,15,7]
head=construct_tree(l)
print(Solution().minDepth(head))