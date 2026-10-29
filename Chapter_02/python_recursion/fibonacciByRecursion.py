def fibonacci(nthNumber):
    # Base Case
    if nthNumber == 1 or nthNumber == 2:
        print('Call to fibonacci(%s). Returning 1.' % nthNumber)
        return 1
    # Recursive Case
    else:
        print('Calling fibonacci(%s) and fibonacci(%s)' % (nthNumber - 1, nthNumber - 2))
        result = fibonacci(nthNumber - 1) + fibonacci(nthNumber - 2)
        print('Call to fibonacci(%s) returning %s' % (nthNumber, result))
        return result


print(fibonacci(10))