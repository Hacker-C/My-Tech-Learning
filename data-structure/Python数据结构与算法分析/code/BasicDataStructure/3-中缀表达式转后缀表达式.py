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


def infixToPostfix(infix: str) -> str:
    """
    中缀转后缀
    """
    dct = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }
    optionStack = Stack()
    ans = []
    for token in infix:
        if token in string.ascii_uppercase:
            ans.append(token)
        elif token == "(":
            optionStack.push(token)
        elif token == ")":
            topToken = optionStack.pop()
            while topToken != "(":
                ans.append(topToken)
                topToken = optionStack.pop()
        else:
            while (not optionStack.isEmpty()) and \
                    dct[optionStack.getTop()] >= dct[token]:
                ans.append(optionStack.pop())
            optionStack.push(token)
    while not optionStack.isEmpty():
        ans.append(optionStack.pop())
    return "".join(ans)


print(infixToPostfix('A+B+C+D'))
