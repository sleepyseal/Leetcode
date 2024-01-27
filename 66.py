class Solution:
    def plusOne(self, digits):
        nums=0
        for i in range(len(digits)-1, -1, -1):
            nums+=digits[i]*pow(10, len(digits)-1-i)
        nums+=1
        def convert2array(num):
            ans=[]
            while num>=10:
                ans.append(num%10)
                num=num//10
            ans.append(num)
            ans.reverse()
            return ans
        return convert2array(nums)