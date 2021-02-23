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


def josephRing(names: list, k: int) -> str:
    """
    :param nums: 人名
    :param k: 要跳过的次数
    :return: 最后活下来的人
    """
    q = LoopQueue(6)
    # 压入堆栈
    for name in names:
        q.enQueue(name)
    while q.size() > 1:
        for i in range(k):
            q.enQueue(q.deQueue())
        # 每次跳过指定次数后，位于队头的出队
        q.deQueue()
        print(q.items)
    return q.deQueue()


if __name__ == "__main__":
    test = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    print(josephRing(test, 7))
