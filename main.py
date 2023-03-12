import math
import random



t = list(map(int, input().split()))
n = int(input())
k = int(input())

sum = 0
sum1 = 0
sum2 = 0
sum3 = 0

for i in range(n):
    sum += math.cos(i * t[1] / n) * (t[1] / n)

for i in range(n):
    sum1 += math.cos((i + 1) * t[1] / n) * (t[1] / n)

for i in range(n):
    sum2 += math.cos((i + 0.5) * t[1] / n) * (t[1] / n)

for i in range(n):
    sum3 += math.cos((i + random.random()) * t[1] / n) * (t[1] / n)


print(math.sin(4))
print(round(sum, 9), round(sum1, 9), round(sum2, 9), round(sum3, 9), sep='\n')
