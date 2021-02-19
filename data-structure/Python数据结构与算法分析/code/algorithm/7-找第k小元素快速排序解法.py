def quick_sort(nums: list) -> list:
    # 基线条件
    if len(nums) < 2:
        return nums
    base_num = nums[0]
    small_nums = [i for i in nums[1:len(nums)] if i < base_num]
    large_nums = [i for i in nums[1:len(nums)] if i > base_num]
    # 进入递归
    return quick_sort(small_nums) + [base_num] + quick_sort(large_nums)


def find_k_num(nums: list, k: int) -> int:
    return quick_sort(nums)[k - 1]


ls = [20, 3, 5, -2, -4, 1, 2, 4,12, 7, -10,9]
print(quick_sort(ls))
print(find_k_num(ls, 9))
