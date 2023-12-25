import numpy
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        account=[0]*3
        for i in bills:
            if i==5:
                account[0]+=1
            if i==10:
                account[0]-=1
                if account[0]<0:
                    return False
                account[1]+=1
            if i==20:
                if account[1]>0:
                    account[0]-=1
                    account[1]-=1
                    if account[0]<0 or account[1]<0:
                        return False
                else:
                    account[0]-=3
                    if account[0]<0:
                        return False
                account[2]+=1
        return True
bills=[5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print(Solution().lemonadeChange(bills))