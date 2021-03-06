class DeQue:
    """
    双端队列
    前端在列表右边
    """
    def __init__(self):
        self.items = []

    def addFront(self, item):
        # 前端入队
        self.items.append(item)

    def addRear(self, item):
        # 后端入队
        self.items.insert(0, item)

    def removeFront(self):
        # 前端出队
        return self.items.pop()

    def removeRear(self):
        # 后端出队
        return self.items.pop(0)

    def size(self):
        # 队列元素个数
        return len(self.items)

    def isEmpty(self):
        # 判空
        return self.size() == []
