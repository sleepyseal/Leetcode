class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total>target:
                        l-=1
                    elif total<target:
                        k+=1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        while k<l:
                            k=k+1
                            if nums[k]!=nums[k-1]:
                                break 
                        while k<l:
                            l=l-1
                            if nums[l]!=nums[l+1]:
                                break 
        return ans
    
nums =[-2,-1,-1,1,1,2,2]
print(Solution().fourSum(nums,0))
