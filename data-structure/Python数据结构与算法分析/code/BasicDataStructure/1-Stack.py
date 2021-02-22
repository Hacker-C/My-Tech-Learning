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


t = Stack()
t.push(123)
t.push('aaa')
print(t)
t.delete()
# print(t)


def brackets_matches1(s: str) -> bool:
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
    if not stk.isEmpty():
        return False
    return True


# print(brackets_matches1('()()(())((()))((()()))'))

def brackets_matches2(s: str) -> bool:
    """
    括号匹配：匹配三种类型括号
    """
    stk = Stack()
    for i in s:
        if i == "(" or i == "[" or i == "{":
            stk.push(i)
        else:  # ) ] }
            if stk.isEmpty():
                return False
            temp = stk.pop()
            if not ((i == ")" and temp == "(")
                    or (i == "]" and temp == "[")
                    or (i == "}" and temp == "{")):
                return False
    if not stk.isEmpty():
        return False
    return True


# print(brackets_matches2("(){}(())[][{()}][({})]()[]{}()[{}]()[()]()()"))
