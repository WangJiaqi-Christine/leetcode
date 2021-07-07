# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:18:59 2021

@author: keikei
"""

"""
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        full = list(range(1,len(nums)+1))
        
        return list(set(full).difference(set(nums)))
        