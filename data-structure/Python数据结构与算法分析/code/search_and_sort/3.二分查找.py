def binSearch(nums, key):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == "__main__":
    print(binSearch([1, 2, 3, 15, 26], 15))
