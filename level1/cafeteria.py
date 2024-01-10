'''
Cafeteria - Facebook Coding Challenge - 1/10/2024

A cafeteria table consists of a row of N seats, numbered from 11 to N from left to right. Social distancing guidelines require that every diner be seated such 
that K seats to their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.There are currently M 
diners seated at the table, the ith of whom is in seat S iNo two diners are sitting in the same seat, and the social distancing guidelines are satisfied. Determine 
the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, 
assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.

'''

from typing import List
import unittest
import calc
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  count=0
  S=S+[0-K]
  S=S+[N+K+1]
  SS=sorted(S)
  for first in list(range(0,len(SS)-1)):
    S1=SS[first]
    S2=SS[first+1]
    openspots=S2-S1-1-2*K
    if openspots>0:
      count+=openspots//(K+1)
      if (openspots % (K+1)):
        count+=1
  return count

print("Result is "+str(getMaxAdditionalDinersCount(10, 1, 2, [2, 6]))+", expected "+ str(3))
print("Result is "+str(getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]))+", expected "+ str(1))