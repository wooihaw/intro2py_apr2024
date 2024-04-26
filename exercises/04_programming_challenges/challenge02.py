# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:01:32 2024

@author: wooihaw
"""

invest = float(input("Enter the initial investment: "))
rate = float(input("Enter the annual rate (%): "))
years = int(input("Enter the years of investment: "))

print(f"Initial investment: RM{invest:.2f}, annual rate: {rate}%, investment years: {years}")

for i in range(years):
    invest = invest + invest * rate/100
    print(f"Year {i+1:>2}: RM{invest:.2f}")