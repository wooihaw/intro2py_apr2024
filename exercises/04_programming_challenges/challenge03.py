# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:10:58 2024

@author: wooihaw
"""

s1 = set(range(5, 101, 5))  # set of numbers divisible by 5
s2 = set(range(7, 101, 7))  # set of numbers divisible by 7
s3 = set(range(1, 101))

print(s3 - (s1 | s2))
