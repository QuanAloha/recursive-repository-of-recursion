def fibonacci(nthNumber):
    a, b = 1, 1
    print('a is %s and b is %s' % (a, b))
    for i in range(1, nthNumber):
        temp = a
        a = b
        b = temp + a
        print('a is %s and b is %s' % (a, b))

    return a


print(fibonacci(10))