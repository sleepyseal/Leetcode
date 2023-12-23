# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        else:
            index=nums.index(max(nums))
            left_arry=nums[0:index]
            if index+1<len(nums):
                right_array=nums[index+1:len(nums)]
            else:
                right_array=[]
            head=TreeNode(nums[index])
            head.left=self.constructMaximumBinaryTree(left_arry)
            head.right=self.constructMaximumBinaryTree(right_array)
            return head

l=[3,2,1,6,0,5]
head=Solution().constructMaximumBinaryTree(l)
print('')