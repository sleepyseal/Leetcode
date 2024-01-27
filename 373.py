class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        def adjust_stack(nums1, nums2, potential_stack):
            if len(potential_stack)<=1:
                return
            save_stack=[]
            ele=potential_stack.pop()
            while potential_stack and nums1[potential_stack[-1][0]]+nums2[potential_stack[-1][1]]>nums1[ele[0]]+nums2[ele[1]]:
                save_stack.append(potential_stack.pop())
            potential_stack.append(ele)
            while save_stack:
                potential_stack.append(save_stack.pop())
            
        saved_pair={}
        potential_stack=[(0,0)]
        saved_pair[(0,0)]=1
        ans=[]
        while len(ans)<k:
            ele=potential_stack.pop(0)
            ans.append([nums1[ele[0]], nums2[ele[1]]])
            if ele[0]+1< len(nums1) and (ele[0]+1, ele[1]) not in saved_pair:
                saved_pair[(ele[0]+1, ele[1])] =1
                potential_stack.append((ele[0]+1, ele[1]))
                adjust_stack(nums1, nums2, potential_stack)
            if ele[1]+1 < len(nums2) and (ele[0], ele[1]+1) not in saved_pair:
                    saved_pair[(ele[0], ele[1]+1)] =1
                    potential_stack.append((ele[0], ele[1]+1))
                    adjust_stack(nums1, nums2, potential_stack)
        return ans
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(Solution().kSmallestPairs(nums1, nums2, k))