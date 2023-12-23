class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def symmetric(self, left, right):
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False
        else:
            b1=self.symmetric(left.left, right.right)
            b2=self.symmetric(left.right, right.left)
            if b1 and b2:
                return True 
            else:
                return False
            
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root.left is None and root.right is not None:
            return False 
        elif root.right is None and root.left is not None:
            return False
        elif root.left.val!=root.right.val:
            return False
        elif root.left.val==root.right.val:
            b=self.symmetric(root.left, root.right)
            return b
            

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
l=[1,2,2,3,4,4,3]
head=construct_tree(l)
print(Solution().isSymmetric(head))
