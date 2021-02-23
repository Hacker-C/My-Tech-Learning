class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def delete(self):
        del self.items

    def __str__(self):
        return '{}'.format(self.items)


def divideByk(num: int, k: int) -> str:
    """
    十进制转k进制
    """
    # 模拟10进制后的进位制
    digits = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    remStack = Stack()
    while num > 0:
        rem = num % k
        if rem > 9:
            rem = digits[rem]
        else:
            rem = str(rem)
        # 将余数（字符）压栈
        remStack.push(rem)
        num //= k
    ans = ''
    while remStack.size():
        # 依次弹出栈中余数
        ans += remStack.pop()
    return ans


print(divideByk(123, 8))
