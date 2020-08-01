x1 = [1,1,0,0]
x2 = [1,0,1,0]
target = [1, -1, -1, -1]
bias = [1,1,1,1]
yin = [2,2,2,2]
y = [2,2,2,2]
w1 = 0
w2 = 0
b = 0

alpha = 1

equal = False

print("x1\t\t\tx2\t\t\tBias\t\t\tyin\t\t\ty\t\t\ttarget\t\t\tw1\t\t\tw2\t\t\tb")
count = 1
while not equal:
    print(f"Iteration # {count}")
    for i in range(4):
        yin[i] = x1[i]*w1 + x2[i]*w2 + b

        if yin[i] > 0:
            y[i] = 1
        elif yin[i] < 0:
            y[i] = -1
        else:
            y[i] = 0

        if y[i] != target[i]:
            w1 = w1 + alpha*target[i]*x1[i]
            w2 = w2 + alpha*target[i]*x2[i]
            b = b + alpha*target[i]

        print(f"{x1[i]}\t\t\t{x2[i]}\t\t\t{bias[i]}\t\t\t{yin[i]}\t\t\t{y[i]}\t\t\t{target[i]}\t\t\t{w1}\t\t\t{w2}\t\t\t{b}")


    if y == target:
        equal = True

    count += 1
