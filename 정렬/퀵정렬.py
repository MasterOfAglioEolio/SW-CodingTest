array=[5,7,9,0,3,1,6,2,4,8]


def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left, right = list(), list()

    for i in range(1, len(data)):
        if data[i] < pivot:
            left.append(data[i])
        else:
            right.append(data[i])

    return qsort(left) + [pivot] + qsort(right)


print(qsort(array))
