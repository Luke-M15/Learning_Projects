# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:56:14 2018

@author: Luke Mottley

Problem: check if a word is a palindrome, the same forwards and backwards
"""

text = input('enter a word: ')

if text == text[::-1]:
    print('{} is a palindrome'.format(text))
else:
    print('{} is not a palindrome'.format(text))
