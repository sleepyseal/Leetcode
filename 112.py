class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        def sum_path(root, s, targetSum):
            if root.left is None and root.right is None:
                if s+root.val ==targetSum:
                    return True
                else:
                    return False
            s=root.val+s
            f1, f2= False, False
            if root.left:
                f1=sum_path(root.left, s, targetSum)
            if root.right:
                f2=sum_path(root.right, s, targetSum)
            if f1 or f2:
                return True
            return False

        return sum_path(root, 0, targetSum)