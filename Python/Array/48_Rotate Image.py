# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:50:59 2021

@author: keikei
"""

"""
You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        
		# reverse matrix upside down
		# select element from bottom to top
        matrix[:] = [ [ row[i] for row in reversed(matrix)] for i in range(len(matrix)) ]