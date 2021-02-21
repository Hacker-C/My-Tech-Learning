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


def brackets_matches(s: str) -> bool:
    """
    特殊情况：一种括号
    """
    stk = Stack()
    for i in s:
        if i == "(":
            stk.push(i)
        else:  # i == ")"
            if not stk.isEmpty():
                if stk.pop() != "(":
                    return False
            else:
                return False
    if stk.size() != 0:
        return False
    return True


print(brackets_matches('()()(())((()))((()()))'))
