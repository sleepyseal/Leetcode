class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        front=0
        back=len(s)-1
        while front<back:
            temp=s[front]
            s[front]=s[back]
            s[back]=temp
            front=front+1
            back=back-1
        return s  
s =["H","a","n","n","a","h"]
print(Solution().reverseString(s))