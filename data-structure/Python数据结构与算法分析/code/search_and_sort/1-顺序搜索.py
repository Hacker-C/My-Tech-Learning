class SSTable:
    # 定义顺序查找表
    def __init__(self, data):
        self.data = data
        self.length = len(self.data)


SST = SSTable([None, 6, 7, 19, 14, 100]) # 第一位不存数据，作为后续哨兵


def searchSeqList(sst, key):
    sst.data[0] = key  # 哨兵
    i = sst.length - 1
    while sst.data[i] != key:
        i -= 1
    # 若返回的i==0，则说明查找失败
    return i


print(searchSeqList(SST, 6))
