class Solution(object):
    def get_left_max(self, height):
        l_max=0
        length=len(height)        
        left_max=[0]*length
        for i in range(1, length):
            if height[i-1]>l_max:
                l_max=height[i-1]
            left_max[i]=l_max
        return left_max
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length=len(height)
        ans=[0]*length
        left_max=self.get_left_max(height)
        # print(left_max)
        height.reverse()
        right_max=self.get_left_max(height)
        right_max.reverse()
        height.reverse()
        # print(right_max)
        for i in range(length):
            ans[i]=max(min(left_max[i],right_max[i])-height[i],0)
        print(sum(ans))
s=Solution()
height= [0,1,0,2,1,0,1,3,2,1,2,1]        
print(s.trap(height))