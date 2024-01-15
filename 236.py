class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root is p or root is q:
            return root
        f1=self.lowestCommonAncestor(root.left, p, q)
        f2=self.lowestCommonAncestor(root.right, p, q)
        if f1 and f2:
            return root
        if f1:
            return f1
        return f2