'''
Write a program that inputs a real number 0 ≤ x ≤ 1 and a number e > 0
and outputs a positive integer n for which |x − {n√2}| < e, assuming that such an n always exists - of
course if there is no such n your program, when run, won’t stop! But experiment anyway.
'''

from math import sqrt, modf
import numpy as np


x = float(input("Please choose a value for x; x is in [0,1]:\n"))
epsilon = float(input("Please choose a value for epsilon; epsilon > 0:\n"))

calculationSize = 1000#00000

nMatrix = np.arange(1,calculationSize)
rootMatrix = np.full((calculationSize-1), sqrt(2))
xMatrix = np.full((calculationSize-1), x)



fracPart = np.modf(np.multiply(nMatrix, rootMatrix))[0]
difference = np.absolute(np.subtract(xMatrix, fracPart))

solutionList = difference[np.where(difference < epsilon)]


if solutionList.size != 0:
	solution = nMatrix[difference.tolist().index(solutionList[0])]
	print("The solution is n = ", solution)
else:
	print("No solution found within calculation range")
	solution = None





if solution != None and abs(x-modf(solution*sqrt(2))[0]) < epsilon:
	print("The solution is correct")

elif solution != None:
	print("The answer is not correct")