# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 23:56:08 2021

@author: keikei
"""

"""
240. Search a 2D Matrix II
Write an efficient algorithm that searches for a target value in an m x n integer matrix. 
The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

********偷懒一行废内存解法********
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return any(target in row for row in matrix)