# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:07:39 2021

@author: keikei
"""

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        res = [0] * l
        
        for i in range(2, l):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                res[i] = res[i-1] + 1
        
        return sum(res)