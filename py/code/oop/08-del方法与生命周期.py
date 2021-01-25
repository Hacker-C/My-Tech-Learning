class Cat:

    def __init__(self, name):
        self.name = name
        print('{}: 我来了'.format(self.name))

    def __del__(self):
        print('{}: 我去了'.format(self.name))


tom = Cat('Tom')
del tom
print('-'*30)
