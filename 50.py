class Solution:
    def myPow(self, x, n):
        def quick_pow(x,n):
            if n==0:
                return 1
            if n==1:
                return x
            y=quick_pow(x, n//2)
            if n%2==0:
                return y*y
            else:
                return y*y*x
        if n>0:
            return quick_pow(x, n)
        return 1/quick_pow(x, -n)
print(Solution().myPow(2.1, 3))