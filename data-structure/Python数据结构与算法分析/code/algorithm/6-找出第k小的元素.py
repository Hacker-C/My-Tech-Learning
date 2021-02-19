def find_k_num(nums: list, k: int) -> int:
    """
    先排序，再取k小元素
    """
    # 冒泡排序
    k -= 1
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums[k]


if __name__ == '__main__':
    ans = find_k_num([4, 2, 5, 1, 3, 8, 9], 5)
    print(ans)

