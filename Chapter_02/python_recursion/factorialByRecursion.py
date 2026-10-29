def factorial(number):
    # Base Case
    if number == 1:
        return 1
    # Recursive Case
    else:
        return number * factorial(number - 1)

print(factorial(5))