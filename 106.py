class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        l=len(inorder)
        if l==0:
            return None
        head=TreeNode(postorder[-1])
        index=inorder.index(postorder[-1])
        left_inorder=inorder[0:index]
        right_inorder=inorder[index+1:]
        left_postorder=postorder[0:index]
        right_postorder=postorder[index:l-1]
        head.left=self.buildTree(left_inorder, left_postorder)
        head.right=self.buildTree(right_inorder, right_postorder)
        return head
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(Solution().buildTree(inorder, postorder))