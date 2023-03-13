import math
import random

funk = input()
leftRange = int(input())
rightRange = int(input())
n = int(input())
method = int(input())


def InegralSum(funk, leftRange, rightRange, n, method):
    sum = 0
    if method == 1:
        funk = funk.replace("x", 'i * (rightRange -  leftRange) / n')
        for i in range(n):
            sum += eval(funk) * ((int(rightRange) - int(leftRange)) / n)
    elif method == 2:
        funk = funk.replace("x", '(i + 1) * (rightRange -  leftRange) / n')
        for i in range(n):
            sum += eval(funk) * ((int(rightRange) - int(leftRange)) / n)
    elif method == 3:
        funk = funk.replace("x", '(i + 0.5) * (rightRange -  leftRange) / n')
        for i in range(n):
            sum += eval(funk) * ((int(rightRange) - int(leftRange)) / n)
    elif method == 4:
        funk = funk.replace("x", "(random.random() + i) * (rightRange -  leftRange) / n")
        for i in range(n):
            sum += eval(funk) * ((int(rightRange) - int(leftRange)) / n)
    return sum


print(InegralSum(funk, leftRange, rightRange, n, 1))
print(InegralSum(funk, leftRange, rightRange, n, 2))
print(InegralSum(funk, leftRange, rightRange, n, 3))
print(InegralSum(funk, leftRange, rightRange, n, 4))