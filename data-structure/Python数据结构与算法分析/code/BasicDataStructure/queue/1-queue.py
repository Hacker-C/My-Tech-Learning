class Queue:
    """
    队列实现
    """

    def __init__(self):
        self.items = []

    def enQueue(self, item):
        return self.items.insert(0, item)

    def deQueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def getHead(self):
        return self.items[len(self.items) - 1]


class LoopQueue:
    """
    循环队列
    """
    def __init__(self, max_size):
        # front指向有数据，rear指向无数据
        self.items = [None] * max_size
        self.front = 0
        self.rear = 0
        self.maxSize = max_size
        self.flag = 0

    def enQueue(self, item):
        if not self.stackFull():
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.maxSize
            self.flag += 1
        return False

    def deQueue(self):
        if not self.isEmpty():
            ans = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.maxSize
            self.flag -= 1
            return ans
        return False

    def size(self):
        return self.flag

    def getHead(self):
        return self.items[self.front]

    def isEmpty(self):
        return self.size() == 0

    def stackFull(self):
        return self.flag == self.maxSize


