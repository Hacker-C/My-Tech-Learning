def recursiveSum(i: int) -> int:
    """
    普通递归
    """
    if i == 1:
        return 1
    return i + recursiveSum(i - 1)


def tailRecursiveSum(i: int, total=0) -> int:
    """
    尾递归
    """
    if i == 1:
        return total
    return tailRecursiveSum(i - 1, total + i)


def iter(i):
    """
    迭代
    """
    ans = 0
    for j in range(1, i+1):
        ans += j
