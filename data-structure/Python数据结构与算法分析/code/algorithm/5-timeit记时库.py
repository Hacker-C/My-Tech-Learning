from timeit import timeit

ls1 = list(range(100000))


ls2 = list(range(200000))

ls3 = list(range(400000))

print(timeit('ls1.pop()', 'from __main__ import ls1', number=1000))
print(timeit('ls2.pop()', 'from __main__ import ls2', number=1000))
print(timeit('ls3.pop()', 'from __main__ import ls3', number=1000))

print('-'*20)
print(timeit('ls1.pop(0)', 'from __main__ import ls1', number=1000))
print(timeit('ls2.pop(0)', 'from __main__ import ls2', number=1000))
print(timeit('ls3.pop(0)', 'from __main__ import ls3', number=1000))
