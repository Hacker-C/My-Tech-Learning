"""
一群猴子要选新猴王。新猴王的选择方法是：
让N只候选猴子围成一圈，从某位置起顺序编号为1~N号。
从第1号开始报数，每轮从1报到3，凡报到3的猴子即退出圈子，接着又从紧邻的下一只猴子开始同样的报数。
如此不断循环，最后剩下的一只猴子就选为猴王。
请问是原来第几号猴子当选猴王？
"""


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


def MonkeyKing(N: int) -> int:
    """
    猴子选大王
    :param N: 参加选王的猴子数
    :return: 选中的猴子序号
    """
    if N <= 2:
        return N
    q = LoopQueue(N)
    for i in range(1, N+1):
        q.enQueue(i)
    while q.size() > 1:
        # 从当前开始计数，所以循环数为3-1==2
        for i in range(2):
            q.enQueue(q.deQueue())
        q.deQueue()
    return q.deQueue()


if __name__ == "__main__":
    print(MonkeyKing(11))

