class Solution:
    def addBinary(self, a, b):
        s=int(a)+int(b)
        def convert2array(num):
            ans=[]
            while num>=10:
                q=num//10
                m=num%10
                ans.append(m)
                num=q
            ans.append(num)
            # ans.reverse()
            return ans
        
        def adjust_array(array):
            for i in range(len(array)-1):
                if array[i]==2 or array[i]==3:
                    array[i]-=2
                    array[i+1]+=1
            if array[-1]>=2:
                array[-1]-=2
                array.append(1)
            array.reverse()
            
        array=convert2array(s)
        adjust_array(array)
        res=''
        for i in array:
            res+=str(i)
        return res
a = "101111"
b = "10"
print(Solution().addBinary(a, b))

