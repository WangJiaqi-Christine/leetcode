# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:47:06 2021

@author: keikei


Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for s_t, t_t in (zip(s, t)):
            if s.index(s_t) != t.index(t_t):
                return False
        
        return True


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
 
        return [s.index(ch) for ch in s] == [t.index(ch) for ch in t]