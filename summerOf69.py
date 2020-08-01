def summerOf69(values):
    indexesOf69 = []
    total = 0
    if 6 in values and 9 in values:
        for i in range(0, len(values)):
            if values[i] == 6 or values[i] == 9:
                indexesOf69.append(i)
           
        for i in range(0, len(values)):
            if i < indexesOf69[0] or i > indexesOf69[1]:
                total += values[i]

        return total
    else:
        return sum(values)


print(summerOf69([2,1,6,9,11]))