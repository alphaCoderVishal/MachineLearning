import pandas as pd
import numpy as np
import math

df = pd.read_csv('kMeansData.csv')
df


def eucldistance(C, X):
    x = C[1]
    x1 = X[1]
    y1 = X[2]
    y = C[2]
    ans1 = x - x1
    ans2 = y - y1
    ans1 = ans1 * ans1
    ans2 = ans2 * ans2
    ans = ans1 + ans2
    ans = math.sqrt(ans)
    return ans


row = len(df)
# into array
arr = np.array(df)
arr
# Initial Seed
K = 3
C1 = arr[0]
C2 = arr[1]
C3 = arr[2]


def compare(x, y, z):
    if x <= y:
        if x <= z:
            return 1
        else:
            return 3
    else:
        if y <= z:
            return 2
        else:
            return 3


Cl1 = [C1]
Cl2 = [C2]
Cl3 = [C3]
# initial
for x in range(3, row - 1):
    dis1 = eucldistance(arr[x], C1)
    dis2 = eucldistance(arr[x], C2)
    dis3 = eucldistance(arr[x], C3)
    r = compare(dis1, dis2, dis3)
    if r == 1:
        Cl1.append(arr[x])
    elif r == 2:
        Cl2.append(arr[x])
    else:
        Cl3.append(arr[x])
x1 = 0
y1 = 0
for x in range(0, len(Cl1)):
    x1 = x1 + Cl1[x][1]
    y1 = y1 + Cl1[x][2]
x1 = x1 / len(Cl1)
y1 = y1 / len(Cl1)
arr1 = ["new", x1, y1]
C1n = arr1
x1 = 0
y1 = 0
arr1 = []
for x in range(0, len(Cl2)):
    x1 = x1 + Cl2[x][1]
    y1 = y1 + Cl2[x][2]
x1 = x1 / len(Cl2)
y1 = y1 / len(Cl2)
arr1 = ["new", x1, y1]
C2n = arr1
x1 = 0
y1 = 0
arr1 = []
for x in range(0, len(Cl3)):
    x1 = x1 + Cl3[x][1]
    y1 = y1 + Cl3[x][2]
x1 = x1 / len(Cl3)
y1 = y1 / len(Cl3)
arr1 = ["new", x1, y1]
C3n = arr1
i = 0
while (i < 10):
    Cl1 = []
    Cl2 = []
    Cl3 = []
    for x in range(0, row - 1):
        dis1 = eucldistance(arr[x], C1)
        dis2 = eucldistance(arr[x], C2)
        dis3 = eucldistance(arr[x], C3)
        r = compare(dis1, dis2, dis3)

        if r == 1:
            Cl1.append(arr[x])
        elif r == 2:
            Cl2.append(arr[x])
        else:
            Cl3.append(arr[x])
    x1 = 0
    y1 = 0
    for x in range(0, len(Cl1)):
        x1 = x1 + Cl1[x][1]
        y1 = y1 + Cl1[x][2]
    x1 = x1 / len(Cl1)
    y1 = y1 / len(Cl1)
    arr1 = ["new", x1, y1]
    C1n = arr1
    x1 = 0
    y1 = 0
    arr1 = []
    for x in range(0, len(Cl2)):
        x1 = x1 + Cl2[x][1]
        y1 = y1 + Cl2[x][2]
    x1 = x1 / len(Cl2)
    y1 = y1 / len(Cl2)
    arr1 = ["new", x1, y1]
    C2n = arr1
    x1 = 0
    y1 = 0
    arr1 = []
    for x in range(0, len(Cl3)):
        x1 = x1 + Cl3[x][1]
        y1 = y1 + Cl3[x][2]
    x1 = x1 / len(Cl3)
    y1 = y1 / len(Cl3)
    arr1 = ["new", x1, y1]
    C3n = arr1
    i = i + 1
# Cluster
print(Cl1)
print(Cl2)
print(Cl3)