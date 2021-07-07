# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:33:36 2021

@author: keikei
"""

"""
Given an array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
     
        i = 1
        j = len(nums)
        
        while i < j:
            total = nums[i-1] + nums[j-1]
            if total == target:
                break
            elif total < target:
                i += 1
            else:
                j -= 1                
        
        return [i, j]