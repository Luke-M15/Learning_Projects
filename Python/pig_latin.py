# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:52:58 2018

@author: Luke Mottley
Problem: convert a word to its pig latin word game version, banana becomes anana-bay
"""

text = input('enter a word: ')

for i, x in enumerate(text):
    if x in ['a','e','i','o','u']:
        pig = text[i:]
        break
    
pig_latin = pig + '-{}ay'.format(text[:i])


print(pig_latin)