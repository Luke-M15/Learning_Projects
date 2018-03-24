# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:33:33 2018

@author: Luke Mottley

Problem: count the number of vowels in some text
"""

text = input('enter a word or some text: ')
a = 0
e = 0
i = 0
o = 0
u = 0
for x in text:
    if x.lower() == 'a':
        a+=1
    elif x.lower() == 'e':
        e+=1
    elif x.lower() == 'i':
        i+=1
    elif x.lower() == 'o':
        o+=1
    elif x.lower() == 'u':
        u+=1

print('The number of vowels is: {}'.format(a+e+i+o+u))
print('The number of As: {}, Es: {}, Is: {}, Os: {} and Us: {}'.format(a,e,i,o,u))
    
