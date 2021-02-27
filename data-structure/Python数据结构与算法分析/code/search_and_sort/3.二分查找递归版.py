def recBinSearch(nums, key):
    if len(nums) == 0:
        return False
    else:
        mid = len(nums) // 2
        if nums[mid] == key:
            return True
        elif nums[mid] < key:
            return recBinSearch(nums[mid + 1:], key)
        else:
            return recBinSearch(nums[:mid], key)


if __name__ == "__main__":
    print(recBinSearch([1, 2, 3, 15, 26], 26))
