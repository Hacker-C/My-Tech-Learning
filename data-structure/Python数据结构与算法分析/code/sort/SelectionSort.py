def selection_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        m = arr[0]
        index = 0
        for j in range(i):
            if arr[j] > m:
                m = arr[j]
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    return arr


if __name__ == '__main__':
    test = [4, 5.0, 34, 123, 3, 13, 5, 123, 37, 19, -3, 0, 37.0]
    print(selection_sort(test))
    # 稳定性：不稳定
    # T(n) = 0(n^2)
