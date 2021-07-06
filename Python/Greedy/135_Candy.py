# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:53:38 2021

@author: keikei
"""

""" 
There are n children standing in a line. 
Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children. 
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        outlist = [1 for i in ratings]
        num = len(ratings)

        for i in range(num-1):
            if ratings[i+1] > ratings[i]:
                outlist[i+1] =  outlist[i] + 1
        
        for i in range(num-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                if outlist[i-1] <= outlist[i]:
                    outlist[i-1] = outlist[i] + 1
        
        return sum(outlist)