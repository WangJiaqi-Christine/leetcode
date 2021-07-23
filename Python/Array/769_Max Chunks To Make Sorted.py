# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 13:04:43 2021

@author: keikei
"""

"""
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
"""

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        end = arr[0]
        
        for i in range(len(arr)):
            end = max(end, arr[i])
            if i == end:
                count +=1
        
        return count

********大佬的一行解法********
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        return sum(max(arr[:i + 1]) == i for i in range(len(arr)))