# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:17:07 2020

@author: 4gutz
"""
savings = 0
count = 0
while savings < 250000:
    savings += (savings * 0.04) / 12
    savings += 1000
    print(savings)
    count += 1
    
print(count)

lst = list(range(1,10001))
print(lst[55])