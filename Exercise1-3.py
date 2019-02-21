"""
Write a program that inputs a positive integer k and outputs an interval [(a−1)/k,a/k], 
with 1 ≤ a ≤ k, that contains two of the terms x_1,..., x_{k+1}. 
"""

from math import sqrt, modf
import numpy as np
import matplotlib.pyplot as plt

k = int(input("Please choose a value for k; k is a positive integer:\n"))

xArray = np.arange(1,k+2)
xArray = np.multiply(xArray, sqrt(2))
xArray = np.modf(xArray)[0]


for i in range(1,k+1):
	plt.axhline(y=i/k)

	countList = []
	for j in xArray:
		if j < i/k and j > (i-1)/k:
			countList.append(j)
	if len(countList) == 2:
		a = i


print("The interval containing two points is: [%s/%s, %s/%s]" % (a-1,k,a,k))

plt.plot(xArray, "ro")
plt.show()
