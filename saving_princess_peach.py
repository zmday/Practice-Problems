# -*- coding: utf-8 -*-
"""Saving Princess Peach.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ptWKWqDrmFrr_vZ7lyAVWs5oTXlKaRIV
"""

#input
import sys
N, Y = map(int, input().split())
if not 0 <= N <= 100:
  sys.exit()
if not 0 <= Y <= 200:
  sys.exit()

list1 = list(range(0, N))
list2 = []
#for-loops to remove obstacles from range
for i in range(Y):
  k = int(input())
  if 0 <= k <= N:
    list2.append(k)
  else:
    sys.exit()
list2 = set(list2)
#for x in list2:
  #list1.remove(x)
#print(*list1, sep = '\n')
#output
list1 = [elem for elem in list1 if not elem in list2]
print(*list1, sep='\n')
print("Mario got",len(list2) , "of the dangerous obstacles.")