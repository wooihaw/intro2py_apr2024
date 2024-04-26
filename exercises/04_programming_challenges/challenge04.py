# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:15:42 2024

@author: wooihaw
"""

def mean(data):
    return sum(data)/len(data)

def median(data):
    sdata = sorted(data)
    n = len(sdata)
    if n%2:
        return sdata[n//2]
    else:
        return (sdata[n//2 - 1] + sdata[n//2]) / 2
    

raw_data = None
with open("data/Heathrow.txt", "r") as f:
    raw_data = f.readlines()
    
if raw_data is not None:
    # print(raw_data)
    data = [float(d.strip()) for d in raw_data]
    # print(data)
    print(f"Lowest temperature: {min(data)}")
    print(f"Highest temperature: {max(data)}")
    print(f"Average temperature: {mean(data)}")
    print(f"Median temperature: {median(data)}")
else:
    print("Error in opening the file")