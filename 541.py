class Solution(object):
    def swap(self, s,start, k):
        s=list(s)
        front=start
        back=front+k-1
        while front<back:
            temp=s[front]
            s[front]=s[back]
            s[back]=temp
            front=front+1
            back=back-1
        s=''.join(s)
        return s 

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=len(s)
        front=0
        back=2*k-1
        while back<n:
            s=self.swap(s,front, k)
            front+=2*k 
            back=front+2*k-1
        rest=n-front
        if rest<=k:
            s=self.swap(s, front, rest)
        else:
            s=self.swap(s, front, k)
        return s
s ='abcdefg'
print(Solution().reverseStr(s, 2))
