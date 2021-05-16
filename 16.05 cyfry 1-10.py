# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:36:03 2021

@author: Joanna
"""

for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            if z==x*2:
                if (x+y+z)%2==1:
                    if x<y and z>y and x<z:
                        print(x,y,z)
                