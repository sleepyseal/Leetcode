class Solution:
    def findKthLargest(self, nums, k):
        def quick_choice(nums, k):
            pivot=nums[0]
            big, equal, small=[],[],[]
            for i in nums:
                if i>pivot:
                    big.append(i)
                elif i<pivot:
                    small.append(i)
                else:
                    equal.append(i)
            if len(big)>=k:
                return quick_choice(big, k)
            elif len(big)+len(equal)<k:
                return quick_choice(small, k-len(big)-len(equal))
            else:
                return pivot
        return quick_choice(nums, k)
arr = [7,6,5,4,3,2,1]
print(Solution().findKthLargest(arr, 2))
print(arr)