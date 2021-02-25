def add(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + add(nums[1:])


if __name__ == "__main__":
    nums = [7, 12, 13, 14, 21, 32]
    print(add(nums))
