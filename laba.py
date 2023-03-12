funk = input()
leftRange = input()
rightRange = input()
n = input()
method = input()
def InegralSum(funk, leftRange, rightRange, n, method):
    sun =0
    if method==1:
        for i in range(n):
            sum+= eval(fun.replace("x", 'i * t[1] / n')) * (t[1] / n)
            fun.replace('i * t[1] / n', "x")
    elif method==2:
        for i in range(n):
            sum+= eval(fun.replace("x", '(i + 1) * t[1] / n')) * (t[1] / n)
            fun.replace('(i + 1) * t[1] / n', "x")
    elif method==3:
        for i in range(n):
            sum+=eval(fun.replace("x", '(i + 0.5) * t[1] / n')) * (t[1] / n)
            fun.replace('(i + 0.5) * t[1] / n', "x")
    elif method==4:
        for i in range(n):
            sum+=eval(fun.replace("x", "random.random() + 1) * t[1] / n")) * (t[1] / n)
            fun.replace("random.random() + 1) * t[1] / n", "x")
    return sum

print(InegralSum(funk, leftRange, rightRange, n, method))