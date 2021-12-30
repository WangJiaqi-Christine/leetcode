# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 15:19:44 2021

@author: keikei
"""

"""
嘻嘻嘻又在偷懒了
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            return -1
