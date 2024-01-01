class Solution:
    def split_num(self, num):
        res=[]
        while num>=10:
            res.append(num%10)
            num=num//10
        res.append(num)
        res.reverse()
        return res 
    
    def monotoneIncreasingDigits3(self, n: int) -> int:
        num=self.split_num(n)
        ans=[num[0]]
        flag=True
        for i in num[1:]:
            if i>=ans[-1]:
                ans.append(i)
            else:
                flag=False
                break
        while not flag and ans:
            ele=ans.pop()
            ele-=1
            if len(ans)==0 or  (len(ans)>=0 and ele>=ans[-1]):
                ans.append(ele)
                break
            elif ans is None:
                ans=[]
        
        for i in range(len(num)-max(len(ans),1)):
            ans.append(9)
        res=0
        time=1
        while ans:
            ele=ans.pop()
            res+=ele*time
            time=time*10
        return res
    
    def monotoneIncreasingDigits2(self, n: int) -> int:
        num=self.split_num(n)
        cmp=0
        flag=True
        for i in range(len(num)):
            if num[i]>=cmp:
                cmp=num[i]
            else:
                flag=False
                break
        if not flag:
            if i==1:
                num[0]=num[0]-1
                ans=[9]*len(num)
                ans[0]=num[0]
                num=ans
            elif i>1 and num[i-1]>=num[i-2]+1:
                num[i-1]=num[i-1]-1
                for j in range(i, len(num),1):
                    num[j]=9
            elif i>1 and num[i-1]<num[i-2]+1:
                while i>1 and num[i-1]<num[i-2]+1:
                    i-=1
                num[i-1]=num[i-1]-1
                for j in range(i, len(num),1):
                    num[j]=9
        res=0
        time=1
        while num:
            ele=num.pop()
            res+=ele*time
            time=time*10
        return res
n = 332
print(Solution().monotoneIncreasingDigits(n))
