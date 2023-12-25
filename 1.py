import numpy
import pandas
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        index=0 
        for i in nums:
            if target-i in d.keys():
                return index, d[(target-i)]
            else:
                d[i]=index
            index=index+1