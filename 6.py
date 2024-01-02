# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows==1:
#             return s
#         res=''
#         time=0
#         l=len(s)
#         index=0
#         ans=''
#         while index<l:
#             if time%(numRows-1)==0:
#                 if index+numRows<=l:
#                     content=s[index:index+numRows]
#                 else:
#                     content=s[index:]
#                 res+=content
#                 index+=numRows
#                 time+=1
#             else:
#                 back_len=time%(numRows-1)*' '
#                 front_len=(numRows-1-len(back_len))*' '
#                 content=front_len+s[index]+back_len
#                 res+=content
#                 index+=1
#                 time+=1
        
#         for k in range(numRows):
#             sub_index=k
#             while sub_index<len(res):
#                 ele=res[sub_index]
#                 if ele!=' ':
#                     ans+=ele
#                 sub_index+=numRows
#         return ans
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

s='PAYPALISHIRING'
numRows=3
print(Solution().convert(s, numRows))