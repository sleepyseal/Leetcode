class Solution:
    def summaryRanges(self, nums):
        ans=[]
        l=len(nums)
        if l==0:
            return [""]
        cur_inter=[]
        for i in range(l):
            if len(cur_inter)==0:
                cur_inter.append(nums[i])
            elif len(cur_inter)>0 and nums[i]-cur_inter[-1]==1:
                cur_inter.append(nums[i])
            else:
                if len(cur_inter)==1:
                    ans.append(str(cur_inter[0]))
                else:
                    ans.append(str(cur_inter[0])+'->'+str(cur_inter[-1]))
                cur_inter=[nums[i]]
        
        if len(cur_inter)==1:
            ans.append(str(cur_inter[0]))
        else:
            ans.append(str(cur_inter[0])+'->'+str(cur_inter[-1]))
        return ans

nums = [0,1,2,4,5,7]
print(Solution().summaryRanges(nums))