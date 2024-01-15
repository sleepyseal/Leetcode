class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.visit=[]
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
        def inorder(root, visit):
            if root is None:
                return
            # if root.left is None and root.right is None:
            #     visit.append(root.val)
            inorder(root.left, visit)
            visit.append(root.val)
            inorder(root.right, visit)
        root=construct_tree(root)
        inorder(root, self.visit)
        self.next_index=0
        self.len=len(self.visit)

    def next(self):
        """
        :rtype: int
        """
        ans=self.visit[self.next_index]
        self.next_index+=1
        print(ans)
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.next_index<self.len:
            return True
        return False
bSTIterator =BSTIterator([7, 3, 15, None, None, 9, 20])
bSTIterator.next()
bSTIterator.next()
bSTIterator.hasNext()
bSTIterator.next()
bSTIterator.hasNext()
bSTIterator.next()
bSTIterator.hasNext()
bSTIterator.next()
bSTIterator.hasNext()