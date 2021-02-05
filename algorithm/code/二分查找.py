def binary_search(ls:list, item:int)->int:
    low = 0
    high = len(ls) - 1
    while low <= high:
        mid = (low + high) // 2
        if ls[mid] == item:
            return mid
        elif ls[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None
print(binnary_search([1,2,3,4,5,6,7,8,9,10], 90))
