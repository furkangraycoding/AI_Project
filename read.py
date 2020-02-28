# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:49:23 2019

@author: Duchess
"""

import pandas as pd
import random as rd
import csv


allLines=[]
i=0
j=0

while j < 6800:
    reviewLine =[]
    i=0
    while i < 10:
        WORDS = ("That was a good movie", "it is interesting", "what a nice job", "perfect acting", " it is a bad movie", "this is fantastic movie ","i loved it"," i think i hated it","it is not good","average movie","I like it")
        word = rd.choice(WORDS)
        reviewLine.append(word)
        i+=1
    print(' '.join(reviewLine))
    allLines.append(' '.join(reviewLine))
    j+=1
print(allLines)
with open('reviews4.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item in allLines:
            writer.writerow([item])
