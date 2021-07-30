# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:53:31 2021

@author: keikei
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l =len(nums)
        
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        
        record = []
        record.extend([nums[0], max(nums[0], nums[1])])

        for i in range(2, l):
            record.append(max(record[i-1], nums[i]+record[i-2])) 
            
        
        return record[l-1]

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l =len(nums)
        
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        
        record = []
        last_2 = nums[0]
        last_1 = max(nums[0], nums[1])

        for i in range(2, l):
            cur = max(last_1, nums[i]+last_2)
            last_2 = last_1
            last_1 = cur
            
        return cur