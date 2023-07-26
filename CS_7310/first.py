'''A5  ch07  NumPy and Pandas'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
# pylint: disable=E0401
import numpy as np
import pandas as pd
import math
import csv
import matplotlib.pyplot as plt

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.sum(axis=0))
print(a.sum(axis=1))

array = np.linspace(2, 10)
print(array)

nn1 = np.array([[1, 2, 3], [4, 5, 6]])
print(nn1[1,0])
print(nn1[1][0])

m1 = np.array([[1, 2, 3], [4, 5, 6]])
print(m1)
print(m1.transpose())
print(m1.T)