class Solution:
    def reverseBits(self, n):
        def num2array(n):
            ans=[]
            while n>=10:
                ans.append(n%10)
                n=n//10
            ans.append(n)
            return ans
        ans=0
        array=num2array(n)
        for i in range(l):
            ans+=pow(2, i)*array[i]
        return ans
n=001
print(Solution().reverseBits(n))