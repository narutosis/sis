import math

t = list(map(int, input().split()))
n = int(input())
k = int(input())

sum = 0
sum1 = 0

for i in range(n):
    sum += math.cos(i * t[1] / n) * (t[1] / n)

for i in range(n):
    sum1 += math.cos((i + 1) * t[1] / n) * (t[1] / n)

print(math.sin(4))
print(round(sum, 6), round(sum, 6), sep='\n')
