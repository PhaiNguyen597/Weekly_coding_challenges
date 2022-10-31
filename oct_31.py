def id_mrtx(n):
    arr = []
    arr2 = []
    try:
        hi = abs(n)
    except:
        return "Error"
    for i in range(abs(n)):
        for j in range(abs(n)):
            arr2.append(0)
        arr.append(arr2)
        arr2 = []

    if n > 0:
        pos = 0
        for i in range(len(arr)):
            arr[i][pos] = 1
            pos += 1
        return arr
    if n < 0:
        pos = abs(n) - 1
        for i in range(len(arr)):
            arr[i][pos] = 1
            pos -= 1
        return arr


print(id_mrtx(50))
