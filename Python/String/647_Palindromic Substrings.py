# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:33:20 2021

@author: keikei
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        l = len(s)
        
        for i in range(l):
            count += 1
            
            if i < (l-1):
                left_i = i-1
                right_i = i+1
                
                while left_i >= 0 and right_i < l:
                    if s[left_i] == s[right_i]:
                        count += 1
                        left_i -= 1
                        right_i += 1
                        
                    else:
                        break
            
                if s[i] == s[i+1]:
                    count += 1
                    left_i = i-1
                    right_i = i+2
                    
                    while left_i >= 0 and right_i < l:
                        if s[left_i] == s[right_i]:
                            count += 1
                            left_i -= 1
                            right_i += 1
                            
                        else:
                            break
        
        return count
                

# %%

# 暴力解法 很慢
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        for end in range(len(s)):
            count += 1
            start=0
            while start < end:
                if s[start:end+1] == s[start:end+1][::-1]:
                    count += 1
                start += 1
        return count

# 和上面逻辑一样，切片写法不一样，注意start=0的时候要换成:
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for end in range(len(s)):
            count += 1
            
            for start in range(end):
                if start > 0:
                    if s[start:end+1] == s[end:start-1:-1]:           
                        count += 1
                        
                else:
                    if s[start:end+1] == s[end::-1]:
                        count += 1   
                        
        return count