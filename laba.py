from main import fun

funk = input()
leftRange = input()
rightRange = input()
n = input()
method = input()
def InegralSum(funk, leftRange, rightRange, n, method):
    sun =0
    if method==1:
        for i in range(n):
            sum+= eval(funk.replace("x", 'i * rightRange -  leftRange / n')) * (rightRange -  leftRange / n)
            fun.replace('i * rightRange -  leftRange / n', "x")
    elif method==2:
        for i in range(n):
            sum+= eval(funk.replace("x", '(i + 1) * rightRange -  leftRange / n')) * (rightRange -  leftRange / n)
            fun.replace('(i + 1) * rightRange -  leftRange / n', "x")
    elif method==3:
        for i in range(n):
            sum+=eval(funk.replace("x", '(i + 0.5) * rightRange -  leftRange / n')) * (rightRange -  leftRange / n)
            fun.replace('(i + 0.5) * rightRange -  leftRange / n', "x")
    elif method==4:
        for i in range(n):
            sum+=eval(funk.replace("x", "random.random() + 1) * rightRange -  leftRange / n")) * (rightRange -  leftRange / n)
            fun.replace("random.random() + 1) * rightRange -  leftRange / n", "x")
    return sum

print(InegralSum(funk, leftRange, rightRange, n, method))