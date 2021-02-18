import time


def test():
    start = time.time()
    for i in range(1000):
        print(1, end='')
    end = time.time()
    print()
    print(-start + end)


if __name__ == "__main__":
    test()