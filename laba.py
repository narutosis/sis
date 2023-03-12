funk = input()
leftRange = input()
rightRange = input()
n = input()
method = input()


def InegralSum(funk, leftRange, rightRange, n, method):
    sum = 0
    if method == 1:
        funk.replace("x", 'i * (rightRange -  leftRange) / n')
        for i in range(n):
            sum += eval(funk) * ((int(rightRange) - int(leftRange)) / n)
    elif method == 2:
        funk.replace("x", '(i + 1) * (rightRange -  leftRange) / n')
        for i in range(n):
            sum += eval(funk) * ((int(rightRange) - int(leftRange)) / n)
    elif method == 3:
        funk.replace("x", '(i + 0.5) * (rightRange -  leftRange) / n')
        for i in range(n):
            sum += eval(funk) * ((int(rightRange) - int(leftRange)) / n)
    elif method == 4:
        funk.replace("x", "(random.random() + 1) * (rightRange -  leftRange) / n")
        for i in range(n):
            sum += eval(funk) * ((int(rightRange) - int(leftRange)) / n)
    return sum


print(InegralSum(funk, leftRange, rightRange, n, method))
