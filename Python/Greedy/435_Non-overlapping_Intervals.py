# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:27:13 2021

@author: keikei
"""
"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        
        end = intervals[0][1]
        rm = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                
            else:
                rm += 1
                end = min(end, intervals[i][1]) #保留end更小的interval，给后面留更多空间
        
        return rm
        