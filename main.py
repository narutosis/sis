import math
import random

fun = input()

t = list(map(int, input().split()))
n = int(input())
k = int(input())

sum = 0
sum1 = 0
sum2 = 0
sum3 = 0

for i in range(n):
    sum += eval(fun.replace("x", 'i * t[1] / n')) * (t[1] / n)
    fun.replace('i * t[1] / n', "x")

for i in range(n):
    sum1 += eval(fun.replace("x", '(i + 1) * t[1] / n')) * (t[1] / n)
    fun.replace('(i + 1) * t[1] / n', "x")

for i in range(n):
    sum2 += eval(fun.replace("x", '(i + 0.5) * t[1] / n')) * (t[1] / n)
    fun.replace('(i + 0.5) * t[1] / n', "x")

for i in range(n):
    sum3 += eval(fun.replace("x", "(random.random() + 1) * t[1] / n")) * (t[1] / n)
    fun.replace("(random.random() + 1) * t[1] / n", "x")

print(math.sin(4))
print(round(sum, 9), round(sum1, 9), round(sum2, 9), round(sum3, 9), sep='\n')
