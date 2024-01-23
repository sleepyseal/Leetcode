# 判断两个区间是否相交：[a, b), [c, d) 
# class Solution:
#     def intersect(interval1, interval2):
#         if interval1[0]<interval2[0]:
#             if interval1[1]>interval2[0]:
#                 return True
#             else:
#                 return False
#         elif interval1[0]==interval2[0]:
#             return True
#         else:
#             if interval2[1]>interval1[0]:
#                 return True
#             else:
#                 return False
