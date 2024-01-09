class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic_num={}
        l=len(nums)
        for i in range(l):
            if nums[i] in dic_num.keys():
                if i-dic_num[nums[i]]<=k:
                    return True
                else:
                    dic_num[nums[i]]=i    
            else:
                dic_num[nums[i]]=i
        return False
nums = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k))