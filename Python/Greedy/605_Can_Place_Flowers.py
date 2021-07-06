# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:39:47 2021

@author: keikei
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        count = 0
        
        flowerbed = [0] + flowerbed + [0] # 头尾补0，省去开头结尾的分类讨论
        
        for i in range(1, len(flowerbed)-1):
            if (flowerbed[i] == 0) and (flowerbed[i-1] == 0) and (flowerbed[i+1] == 0):
                count += 1
                flowerbed[i] = 1
        
        return count>=n
             
             