# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:57:28 2024

@author: wooihaw
"""

# c - chicken
# r - rabbit
# c + r = 35
# 2*c + 4*r = 94

for r in range(36):
    c = 35 - r
    if 2*c + 4*r == 94:
        print(f"There are {c} chickens and {r} rabbits in the farm.")
        break