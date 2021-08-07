# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

import random as rd

import matplotlib.pyplot as plt

sidedie = [];

# number of die as input

# number of elements
n = int(input("Enter number of die you would like to roll: "))
  
# Below line read inputs from user using map() function 
sidedie = list(map(int,input("\nEnter the number of sides on each die as numbers separated by spaces : ").strip().split()))[:n]
  
print("\nThe die will have sides: ", sidedie)

J = int(input("How many mulitples of the number of microstates (N) would you like to roll?"))

# number of microstates for system

N = np.product(sidedie);

maxroll = np.sum(sidedie);

# list to dump roll results

rolls = np.zeros((N*J, n));

# die roll loop

for i in range(N*J): 
    for j in range(n):
        rolls[i, j] = rd.randint(1, sidedie[j]);
        
# roll sums

total = np.sum(rolls, axis = 1);

plt.hist(total, bins = range(n,maxroll), density = True, 
         histtype ='bar', rwidth = 0.5)
plt.xlabel("microstate")
plt.ylabel("W")
        
        

    

