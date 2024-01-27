class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        mid_index=len(nums)//2
        root= TreeNode(nums[mid_index])
        root.left=self.sortedArrayToBST(nums[:mid_index])
        root.right=self.sortedArrayToBST(nums[mid_index+1:])
        return root

nums=[-10,-3,0,5,9]
print(Solution().sortedArrayToBST(nums))