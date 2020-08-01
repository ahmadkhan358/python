def two_sum_brute_force(target, list):
    indices = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i]+list[j] == target:
                indices.append(i)
                indices.append(j)
                return indices


def two_sum(target, list):
    dict = {}
    for i in range(len(list)):
        if target-list[i] not in dict:
            dict[list[i]] = i
        else:
            return [dict[target-list[i]], i]


x = two_sum(10, [2,1,8,9])
print(x)