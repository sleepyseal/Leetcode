class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        def convert2array(num):
            ans=[]
            while num>=10:
                ans.append(num%10)
                num=num//10
            ans.append(num)
            return ans
        array=convert2array(x)
        left, right=0, len(array)-1
        while left<right:
            if array[left]==array[right]:
                left+=1
                right-=1
            else:
                return False
        return True