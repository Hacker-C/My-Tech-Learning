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

q = Queue()
