class Solution:
    def findKthLargest(self, nums, k):
        if len(nums)==1:
            return nums[0]
        def swap(nums, left, right):
            temp=nums[left]
            nums[left]=nums[right]
            nums[right]=temp
        def quick(nums, left, right, find, k):
            if left>=right or find[0] >0:
                return
            pivot=nums[left]
            i, j= left, right
            while i<j:
                while i<j and nums[j]>=pivot:
                    j-=1
                while i<j and nums[i]<=pivot:
                    i+=1
                if i<j:
                    swap(nums, i, j)
            if len(nums)-i==k:
                find[0]=pivot
                return
            else:
                swap(nums, left, i)
                if i>len(nums)-k:
                    quick(nums, left, i-1, find, k)
                else:
                    quick(nums, i+1, right, find, k)
        find=[-1]
        quick(nums, 0, len(nums)-1, find, k)
        if find[0]==-1:
            return(nums[len(nums)-k])
        return find[0]
arr = [7,6,5,4,3,2,1]
print(Solution().findKthLargest(arr, 5))
print(arr)