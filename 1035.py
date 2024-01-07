class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        l1, l2= len(nums1)+1, len(nums2)+1
        dp=[]
        ans=0
        for i in range(l1):
            dp.append([0]*l2)
        for i in range(1, l1):
            for j in range(1, l2):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    if dp[i][j]>ans:
                        ans=dp[i][j]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        return ans