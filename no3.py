# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:16:26 2019

@author: Ahmad Luthfi Mahar
"""

def nomor3(als):
    prima = [2, 3, 5, 7, 11, 13,17, 19, 23, 29]
    for j in range(als):
        print('\n', end='')
        for i in range(j+1):
            print(prima[i], end='')

nomor3(5)