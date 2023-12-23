# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         ans=[]
#         element= s.split(' ')
#         num=len(element)
#         for i in range(num-1,-1,-1):
#             if len(element[i])>0:
#                 ans.append(element[i]+' ')
#         ans=''.join(ans)
#         ans=ans[:-1]
#         return ans
class Solution(object):
    def reverse(self, s, start, end):
        while start<end:
            temp=s[start]
            s[start]=s[end]
            s[end]=temp
            start+=1
            end-=1
        return s 
    
    def reverseWords(self, s):
        fast, slow=0,0 
        list_s=list(s)
        start=True
        while start:
            if list_s[fast]==' ':
                fast=fast+1
            else:
                list_s[slow]=list_s[fast]
                fast=fast+1
                slow=slow+1
                start =False
        while fast<len(list_s):

            if list_s[fast]!=' ':
                list_s[slow]=list_s[fast]
                fast=fast+1
                slow=slow+1
            elif list_s[fast]==' ' and list_s[fast-1]!=' ':
                list_s[slow]=' '
                fast=fast+1
                slow=slow+1
            elif list_s[fast]==' ' and list_s[fast-1]==' ':
                fast=fast+1

        list_s=list_s[:slow]
        if list_s[-1]==' ':
            list_s=list_s[:-1]
        list_s=self.reverse(list_s, 0, len(list_s)-1)
        start=0
        end=0
        for i in list_s:
            if i !=' ':
                end+=1
            else:
                list_s=self.reverse(list_s, start, end-1)
                start=end+1
                end=end+1
            
            if end==len(list_s)-1:
                list_s=self.reverse(list_s, start, end)
        s=''.join(list_s)
        return s

s= "a"
print(Solution().reverseWords(s))