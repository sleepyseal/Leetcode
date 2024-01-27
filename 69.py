class Solution:
    def mySqrt(self, x):
        if x<2:
            return x
        left,right=0, x
        def is_valid(sqr, x):
            if (sqr**2<x and (sqr+1)**2>x):
                return True
            return False
        while left<right:
            mid=(left+right)//2
            sqr_mid=mid**2
            if sqr_mid==x or is_valid(mid, x):
                return mid
            elif sqr_mid<x:
                left=mid+1
            else:
                right=mid