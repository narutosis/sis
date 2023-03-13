import math
import random
import matplotlib.pyplot as plt

funk = input()  # функция
leftRange = int(input())  # левая граница
rightRange = int(input())  # правая граница
n = int(input())  # размер разбиения
method = int(input())  # способ выбора оснащения


def InegralSum(funk, leftRange, rightRange, n, method):

    if method == 1:  # левые точки отрезка
        funkSum = funk + " "
        funkSum = funkSum.replace("x", 'i * (rightRange -  leftRange) / n')
        return Grafix(funk, funkSum, leftRange, rightRange, n)

    elif method == 2:  # правые точки отрезка
        funkSum = funk
        funkSum = funkSum.replace("x", '(i + 1) * (rightRange -  leftRange) / n')
        return Grafix(funk, funkSum, leftRange, rightRange,  n)

    elif method == 3:  # средние точки отрезка
        funkSum = funk
        funkSum = funkSum.replace("x", '(i + 0.5) * (rightRange -  leftRange) / n')
        return Grafix(funk, funkSum, leftRange, rightRange, n)

    elif method == 4:  # случайные точки отрезка
        funkSum = funk
        funkSum = funkSum.replace("x", "(random.random() + i) * (rightRange -  leftRange) / n")
        return Grafix(funk, funkSum, leftRange, rightRange, n)

def Grafix(funk, funkSum, leftRange, rightRange, n):
    sum = 0
    X = [0] * n
    funkY = [0] * n
    funkSumY = [0] * n
    x = leftRange
    for i in range(0,n):
        x += (rightRange-leftRange)/n
        X[i] = x
        funkY[i] = eval(funk)
        sum += eval(funkSum) * ((int(rightRange) - int(leftRange)) / n)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(X, funkY, label="funk")
    plt.legend()
    print()
    plt.show()
    return sum


print(InegralSum(funk, leftRange, rightRange, n, method))
print(InegralSum(funk, leftRange, rightRange, n, 2))
print(InegralSum(funk, leftRange, rightRange, n, 3))
print(InegralSum(funk, leftRange, rightRange, n, 4))
