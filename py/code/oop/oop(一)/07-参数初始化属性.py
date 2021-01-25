class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{}爱吃鱼".format(self.name))


tom = Cat('tom')
lazy = Cat('大懒猫')
tom.eat()
lazy.eat()
