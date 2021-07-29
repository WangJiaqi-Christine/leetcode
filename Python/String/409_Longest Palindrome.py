# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:38:29 2021

@author: keikei

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = set()
        
        for i in s:
            if i not in check:
                check.add(i)
            else: 
                check.remove(i)
        
        return len(s)-len(check)+1 if check else len(s)