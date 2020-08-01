def blackJack(x, y, z):
    if (x+y+z) <= 21:
        return x+y+z
    elif (x+y+z) > 21 and 11 in (x, y, z):
        return (x+y+z) - 10
    else:
        return 'BUST'


print(blackJack(11, 11, 11))