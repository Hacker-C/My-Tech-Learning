class Node:
    """
    结点类
    """

    def __init__(self, init_data):
        # 定义结点的数据域和指针域
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next


class LinkList:
    """
    单链表类
    """

    def __init__(self):
        # 头指针
        self.head = None

    def isEmpty(self):
        return self.head is None

    def headInsert(self, data):
        # 头插法建表
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        # 求表长，基于遍历
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def printList(self):
        # 打印链表，基于遍历
        current = self.head
        print('表头[', end='')
        while current is not None:
            print(current.data, end=' ')
            current = current.getNext()
        print(']表尾')

    def search(self, e):
        # 搜索，基于遍历
        current = self.head
        while current is not None:
            if current.data == e:
                return True
            current = current.getNext()
        return False

    def removeElem(self, e):
        # 移除数据值为e的结点，基于遍历
        current = self.head
        if current.data == e:
            self.head = current.getNext()
            return True
        precious = self.head
        current = current.getNext()
        while current is not None:
            if current.data == e:
                precious.setNext(current.getNext())
                return True
            precious = current
            current = current.getNext()
        return False


lst = LinkList()
lst.headInsert(10)
lst.headInsert(11)
lst.headInsert(12)
lst.headInsert(13)
lst.printList()
print(lst.isEmpty())
print(lst.length())
print(lst.search(12))
lst.removeElem(11)
lst.printList()
lst.removeElem(13)
lst.printList()
lst.removeElem(10)
lst.printList()


