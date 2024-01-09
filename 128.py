class Solution:
    def longestConsecutive(self, nums):
        dic_n={}
        if len(nums)==0:
            return 0
        ans=1
        for i in nums:
            if i not in dic_n:
                dic_n[i]=' '
        
        for i in dic_n:
            if i-1 not in dic_n:
                cur_length=1
                cur_num=i
                while cur_num+1 in dic_n:
                    cur_num=cur_num+1
                    cur_length+=1
                    if cur_length>ans:
                        ans=cur_length
        return ans