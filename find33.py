def find33(values):
    for i in range(0, len(values)):
        if values[i] == 3 and values[i+1] == 3:
            return True

    return False  


print(find33([1,2,3,3,4,5]))

# find33([1,2,3,3,4])