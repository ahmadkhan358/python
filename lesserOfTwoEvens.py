def lesserOfTwoEvens(num1, num2):
    evenOrOdd1 = num1 % 2
    evenOrOdd2 = num2 % 2

    if evenOrOdd1 == 1 or evenOrOdd2 == 1:
        return max(num1, num2)

    else:
        return min(num1, num2)



print(lesserOfTwoEvens(6, 3))