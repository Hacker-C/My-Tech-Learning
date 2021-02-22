import string


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def getTop(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def delete(self):
        del self.items

    def __str__(self):
        return '{}'.format(self.items)


def postFixExpr(postfix: str) -> float:
    """
    计算后缀表达式（只涉及整数运算加减乘除）
    """
    numsStack = Stack()
    for i in postfix:
        if i in string.digits:
            # '0123456789'
            numsStack.push(i)
        else:
            # 弹出最近的两个数，注意先弹出的a是右操作数
            a = numsStack.pop()
            b = numsStack.pop()
            # eval计算中缀表达式的值并压入堆栈
            numsStack.push(str(eval(b+i+a)))
    # 此时堆栈中只剩一个数，即为返回值
    return eval(numsStack.pop())


print(postFixExpr('78+32+/'))