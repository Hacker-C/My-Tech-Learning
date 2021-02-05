def selectionSort(arr):
    l = len(arr)
    k = 0
    while k < l:
        index = k
        for i in range(k, l):
            if arr[i] < arr[index]:
                index = i
        arr[k], arr[index] = arr[index], arr[k]
        k += 1
    return arr

sortA=selectionSort([12,1,4,2,5,6,61,3,56,6,16])
print(sortA)
