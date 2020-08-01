def almostThere(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(almostThere(122))