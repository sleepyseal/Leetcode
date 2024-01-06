class Solution:
    def  findLength(self, nums1, nums2):
        l1, l2=len(nums1), len(nums2)
        dp=[]
        ans=0
        for i in range(l1+1):
            dp.append([0]*(l2+1))
        for i in range(l1):
            for j in range(l2):
                if nums1[i]==nums2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                    if dp[i+1][j+1]>ans:
                        ans=dp[i+1][j+1]
                else:
                    dp[i+1][j+1]=0
        return ans
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
print(Solution().findLength(nums1, nums2))