from timeit import timeit


def test1():
    ls = []
    for i in range(10000):
        ls.append(i)


t1 = timeit('test1()', 'from __main__ import test1', number=1)
print(t1)
