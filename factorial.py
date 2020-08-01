def factorial(number):
    fact = 1
    for i in range(number, 1, -1):
        fact *= i

    return fact


print(factorial(10))