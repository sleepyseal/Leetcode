class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        temp=root.left
        root.left=root.right
        root.right=temp 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
def construct_tree(lst):
    if lst is None:
        return 
    queue=[]
    head=TreeNode(lst[0])
    queue.append(head)
    i=0
    while i < (len(lst)):
        while queue:
            ele=queue.pop(0)
            i+=1
            if i<len(lst):
                if lst[i] is not None:
                    new=TreeNode(lst[i])
                    queue.append(new)
                    ele.left=new
            i+=1
            if i<len(lst):
                if lst[i] is not None:
                    new=TreeNode(lst[i])
                    queue.append(new)
                    ele.right=new
    return head
l=[4,2,7,1,3,6,9]
head=construct_tree(l)
head=Solution().invertTree(head)
print('')



        