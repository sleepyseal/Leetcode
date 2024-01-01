# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return inf, 0, 0
            l_choose, l_fa, l_chi= dfs(node.left)
            r_choose, r_fa, r_chi= dfs(node.right)

            choose=1+min(l_choose, l_fa, l_chi)+min(r_choose, r_fa, r_chi)
            fa=min(l_choose, l_chi)+min(r_choose, r_chi)
            chi=min(l_choose+r_choose, l_choose+r_chi, l_chi+r_choose)
            return choose, fa, chi
        a, b, c= dfs(root)
        return min(a, c)