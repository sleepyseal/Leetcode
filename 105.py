class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None
        node=TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                left_tree=inorder[0:i]
                right_tree=inorder[i+1:]
                left_pre=preorder[1:i+1]
                right_pre=preorder[i+1:]
                break
        node.left=self.buildTree(left_pre, left_tree)
        node.right=self.buildTree(right_pre, right_tree)
        return node
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]         
print(Solution().buildTree(preorder, inorder))       