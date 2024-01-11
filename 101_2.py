class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        stack=[]
        def layer_symm(stack):
            l=len(stack)
            first, tail=0, l-1
            while first<tail:
                if stack[first]!=stack[tail]:
                    return False
                first+=1
                tail-=1
            return True
        node=root
        node_stack=[]
        if node is None:
            return True
        else:
            node_stack.append(node)
            l=len(node_stack)
            cur_l=0
            while len(node_stack)>0:
                ele=node_stack.pop(0)
                if ele is not None:
                    stack.append(ele.val)
                    node_stack.append(ele.left)
                    node_stack.append( ele.right)
                    cur_l+=2
                else:
                    stack.append('#')
            
                l-=1
                if l==0:
                    if layer_symm(stack) is False:
                        return False
                    else:
                        l=cur_l
                        cur_l=0
                        stack=[]
            return True

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