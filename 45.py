class Solution(object):
    def max_ele(self, nums):
        if len(nums)==0:
            return -1
        else:
            max_element=-1
            index=-1
            for i in range(len(nums)):
                if nums[i]>=max_element:
                    max_element=nums[i]
                    index=i
            return max_element, index
        
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        skip=[0]*len(nums)
        count=0
        for i in nums:
            skip[count]=count+i 
            count=count+1
        index=0
        time=1
        right_most=skip[index]
        while right_most<len(nums)-1:
            sub_nums=skip[index+1:index+nums[index]+1]
            max_element, index_bias =self.max_ele(sub_nums)
            index+=index_bias+1
            right_most=index+nums[index]
            time+=1

        return time

nums=[5,9,3,2,1,0,2,3,3,1,0,0]
print(Solution().jump(nums))


