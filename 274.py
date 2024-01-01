# class Solution:
#     def hIndex(self, citations):
#         l=len(citations)
#         if l==1:
#             return min(1, citations[0])
#         citations.sort()

#         count=0
#         for i in citations:
#             if i >0:
#                 break
#             else:
#                 count+=1
#         citations=citations[count:]

#         l=l-count
#         if l==0:
#             return 0
#         for i, v in enumerate(citations):
#             if l-i<v:
#                 break
#             elif l-i==v:
#                 return v
#         return min(citations[i], l-i)
    
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citation = sorted(citations, reverse = True)
        h = 0; i = 0; n = len(citations)
        while i < n and sorted_citation[i] > h:
            h += 1
            i += 1
        return h

citations = [4,4,0,0]
print(Solution().hIndex(citations))