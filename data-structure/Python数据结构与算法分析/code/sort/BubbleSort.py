def bubble_sort(arr):
    l = len(arr)
    for i in range(l - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    test = [34, 123, 3, 13, 5, 19, -3, 0, 37]
    print(bubble_sort(test))
