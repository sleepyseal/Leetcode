from collections import defaultdict
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total>0:
                    k-=1
                elif total<0:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j<k:
                        j+=1
                        if nums[j]!=nums[j-1]:
                            break 
                    while j<k:
                        k-=1
                        if nums[k]!=nums[k+1]:
                            break

        return ans

nums =[-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

