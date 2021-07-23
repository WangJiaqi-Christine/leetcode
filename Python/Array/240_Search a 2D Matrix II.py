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

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        i, j = len(matrix)-1, 0
        
        while (i >= 0) and (j <= len(matrix[0])-1):
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] >= target:
                i -= 1
                
            else:
                j += 1
        
        return False
    
    
********偷懒一行废内存解法********
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        return any(target in row for row in matrix)

********再不好好刷LC就得去街边喝西北风了********