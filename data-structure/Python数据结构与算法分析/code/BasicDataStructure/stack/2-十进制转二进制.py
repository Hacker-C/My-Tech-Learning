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


def divide_by2(num):
    # 建栈
    s = Stack()
    # 循环除以2
    while num > 0:
        rem = num % 2
        # 依次压栈
        s.push(rem)
        num //= 2
    ans = ''
    while s.size():
        # 依次出栈
        ans += str(s.pop())
    return int(ans)


print(divide_by2(25))