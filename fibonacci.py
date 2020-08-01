def fibonacci(upto):
    fiboList = [0,1]
    
    for i in range(2, upto+1):
        newNum = (fiboList[i-1]) + (fiboList[i-2])
        fiboList.append(newNum)
        
    return fiboList


print(fibonacci(10))