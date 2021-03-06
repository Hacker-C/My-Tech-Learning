class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        print("[{}]跑了一次步。".format(self.name))
        self.weight -= 0.5

    def eat(self):
        print("[{}]吃了一次东西。".format(self.name))
        self.weight += 1

    def __str__(self):
        return "[{}]现在重量为{}。".format(self.name, self.weight)


XiaoMing = Person('小明', 75.0)
XiaoMei = Person('小美', 45.0)
XiaoMei.run()
XiaoMing.eat()
print(XiaoMing)
print(XiaoMei)