from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  total=0
  for sublist in G:
    total=total+sum(sublist)
  return total/R/C