# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:53:40 2021

@author: keikei
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 3:
            return n
        
        i_2 = 1
        i_1 = 2
        
        for i in range(3, n+1):
            result = i_2 + i_1
            i_2 = i_1
            i_1 = result
        
        return i_1