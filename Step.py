import pandas as pd
import numpy as np
ds = [['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'yes'],
      ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'yes'],
      ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'no'],
      ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'yes']]
for i in range(len(ds)):
    if ds[i][-1] == 'yes':
        temp = ds[i]
        print(ds[i])
        break
for j in range(len(ds)):
    if ds[i][-1] == 'yes':
        for index, val in enumerate(ds[j]):
            if val != temp[index]:
                temp[index] = '?'
print(temp)






# for row in range(len(ds)):
#     row1 = row+1
#     for row1 in range(len(ds)):
#         print(row, row1)
# for i in range(len(ds)):
#     if ds[i][-1] == "yes":
#         for j in range(len(ds[i])):
#             if ds[j][-1] == "yes":
#                 print(ds[i])
# for i, val in enumerate(ds):
#   if val == 'yes':
#       specific_hypothesis = c[i].copy()





# def fun(c, ds):
#     for i, val in enumerate(ds):
#         if val == "Yes":
#             specific_hypothesis = c[i].copy()
#     break
#
#     for i, val in enumerate(c):
#         if ds[i] == "Yes":
#             for x in range(len(specific_hypothesis)):
#             if val[x] != specific_hypothesis[x]:
#             specific_hypothesis[x] = '?'
#     else:
#         pass
#     return specific_hypothesis


# print(" The final hypothesis is:", train(a, t))
















