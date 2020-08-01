numbers = [1,2,3,4,5,6]

print(list(map(lambda num: num**2, numbers)))


print(list(filter(lambda num: num%2 == 0, numbers)))