class Solution:
    def isHappy(self, n):
        def convert_array(n):
            res=[]
            while n>=10:
                res.append(n%10)
                n=n//10
            res.append(n)
            res.reverse()
            return res
        def convert_num(num):
            res=0
            for i in num:
                res+=pow(i,2)
            return res
        list_n=[n]
        while True:
            array_n=convert_array(n)
            n=convert_num(array_n)
            if n==1:
                return True
            if n in list_n:
                return False
            else:
                list_n.append(n)
n=19
print(Solution().isHappy(n))

