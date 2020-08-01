import math

heightXweight = [
    [185, 72],
    [170, 56],
    [168, 60],
    [179, 68],
    [182, 72],
    [188, 77],
    [180, 71],
    [180, 70],
    [183, 84],
    [180, 88],
    [180, 67],
    [177, 76]
]

c1 = [heightXweight[0]]
c2 = [heightXweight[1]]

centroidc1 = [185, 72]
centroidc2 = [170, 56]

for i in range(2, 12):
    update = []
    
    xcordc1 = heightXweight[i][0] - centroidc1[0]
    ycordc1 = heightXweight[i][1] - centroidc1[1]

    dc1 = math.sqrt((xcordc1*xcordc1) + (ycordc1*ycordc1))

    xcordc2 = heightXweight[i][0] - centroidc2[0]
    ycordc2 = heightXweight[i][1] - centroidc2[1]

    dc2 = math.sqrt((xcordc2*xcordc2) + (ycordc2*ycordc2))

    if dc1 < dc2:
        c1.append(heightXweight[i])
        update = c1
    else:
        c2.append(heightXweight[i])
        update = c2

    x = 0
    y = 0
    length = len(update)
    for j in update:
        x += j[0]
        y += j[1]

    if update == c1:
        centroidc1[0] = x / length
        centroidc1[1] = y / length
    else:
        centroidc2[0] = x / length
        centroidc2[1] = y / length

print(c1)
print(c2)

        
