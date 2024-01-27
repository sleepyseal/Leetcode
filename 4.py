class Solution:
    def binary_search(self, nums, target):
        left, right=0, len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return left
    
    def findMedianSortedArrays(self, nums1, nums2):
        m, n= len(nums1), len(nums2)
        target_index=(m+n)//2
        l1, l2, r1, r2=0,0, m, n
        f1, f2=False, False
        while l1<r1 and l2<r2:
            m1=(l1+r1)//2
            m2=(l2+r2)//2
            pos_m1_in_n2=self.binary_search(nums2, nums1[m1])
            pos_m2_in_n1=self.binary_search(nums1, nums2[m2])
            if (pos_m1_in_n2+m1)<target_index:
                l2=pos_m1_in_n2+1
            elif (pos_m1_in_n2+m1)>target_index:
                r2=pos_m1_in_n2
            else:
                l2=pos_m1_in_n2
                f2=True
                break
            if (pos_m2_in_n1+m2)<target_index:
                l1=pos_m2_in_n1+1
            elif (pos_m2_in_n1+m2)>target_index:
                r1=pos_m2_in_n1
            else:
                l1=pos_m2_in_n1
                f1=True
                break
        if f1 is False and f2 is False:
            if l1>=r1:
                goal_index=target_index-m
                if (m+n)%2==0:
                    return (nums2[goal_index]+nums2[goal_index-1])/2
                else:
                    return nums2[goal_index]
            else:
                goal_index=target_index-n
                if (m+n)%2==0:
                    return (nums1[goal_index]+nums1[goal_index-1])/2
                else:
                    return nums1[goal_index]
        elif f1:
                if (m+n)%2==0:
                    return (nums1[l1]+nums1[l1-1])/2
                else:
                    return nums1[l1]
        else:
                if (m+n)%2==0:
                    return (nums2[l2]+nums2[l2-1])/2
                else:
                    return nums2[l2]

nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))