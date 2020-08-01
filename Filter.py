def checkEven(num):
    return num%2 == 0


numbers = [1,2,3,4,5,6]

print(list(filter(checkEven, numbers)))
