class Cat:

    def __init__(self, name):
        self.name = name
        print('{}: 我来了'.format(self.name))

    def __del__(self):
        print('{}: 我去了'.format(self.name))

    def __str__(self):
        # 必须返回字符串
        return '我是小猫[{}]'.format(self.name)


tom = Cat('Tom')
print(tom)
