# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:47:14 2021

@author: keikei
"""

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        starts = set('[{(')
        pairs = (('[', ']'), ('{', '}'), ('(', ')'))
        check = []
        
        for i in s:
            if i in starts:
                check.append(i)
                
            elif (len(check) == 0) or ((check[-1], i) not in pairs):
                return False
            
            else:
                check.pop()
        
        return not check
                    