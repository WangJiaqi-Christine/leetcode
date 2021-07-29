# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 22:18:23 2021

@author: keikei
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        return haystack.find(needle)

# 比上面慢很多，内存也稍多
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
