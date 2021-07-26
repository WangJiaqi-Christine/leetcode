# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 23:36:12 2021

@author: keikei
"""

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        check_dict = {}
        
        for i in s:
            if i in check_dict:
                check_dict[i] += 1
            else:
                check_dict[i] = 1
        
        for i in t:
            if i not in check_dict or check_dict[i] == 0:
                return False
            else:
                check_dict[i] -= 1
        
        for val in check_dict.values():
            if val != 0:
                return False
                
        return True