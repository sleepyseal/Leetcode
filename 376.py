class Solution(object):
    def compare(self, arr):
        if arr[-2]<arr[-1]:
            return -1
        else:
            return 1 # 3 1

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        ans.append(nums[0])
        j=1
        while j<len(nums):
            if nums[j]!=nums[0]:
                ans.append(nums[j])
                break 
            j+=1
        if len(ans)==1:
            return len(ans)
        flag=self.compare(ans)
        for i in range(j, len(nums), 1):
            if flag==1 and ans[-1]<nums[i]:
                ans.append(nums[i])
                flag=-1
            elif flag==1 and ans[-1]>nums[i]:
                ans[-1]=nums[i]
            elif flag==-1 and ans[-1]<nums[i]:
                ans[-1]=nums[i]
            elif flag==-1 and ans[-1]>nums[i]:
                ans.append(nums[i])
                flag=1
        return len(ans)
nums = [3,3,3,2,5]
print(Solution().wiggleMaxLength(nums))