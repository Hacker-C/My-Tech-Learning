class SSTable:
    # 定义顺序查找表
    def __init__(self, data):
        self.data = data
        self.length = len(self.data)


SST = SSTable([1, 3, 7, 13, 42, 100])


def searchSeqList2(sst, key):
    for i in range(sst.length):
        print(sst.data[i])
        if sst.data[i] == key:
            return i
        if sst.data[i] > key:
            # 若此时元素值大于key，则直接返回
            return False
    return False


print(searchSeqList2(SST, 13))
