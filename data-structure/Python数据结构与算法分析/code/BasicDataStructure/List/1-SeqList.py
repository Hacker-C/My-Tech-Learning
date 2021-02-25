class SeqList:
    """
    顺序表
    """

    def __init__(self):
        # 用python列表实现顺序表
        self.data = []

    def length(self):
        # 返回表长
        return len(self.data)

    def locateElem(self, e):
        # 按值查找
        return e in self.data

    def getElem(self, i):
        # 按索引查找
        if i < self.length():
            return self.data[i]
        return None

    def listInsert(self, i, e):
        # 插入指定位置
        if i <= self.length():
            self.data.insert(i, e)
            return True
        return False

    def printList(self):
        if not self.isEmpty():
            return "表头-{}-表尾".format(self.data)
        return None

    def isEmpty(self):
        return self.data == []

    def destroyList(self):
        del self.data


lst = SeqList()
lst.listInsert(0, 10)
lst.listInsert(1, 11)
lst.listInsert(2, 12)
print(lst.printList())
lst.listInsert(2, 99)
print(lst.printList())
lst.listInsert(4,100)
print(lst.printList())
