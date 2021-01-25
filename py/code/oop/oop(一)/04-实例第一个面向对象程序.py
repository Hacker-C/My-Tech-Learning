class Cat:

    def eat(self):
        print('小猫爱吃鱼')

    def drink(self):
        print('小猫要喝水')


# tom对象
tom = Cat()
tom.drink()
tom.eat()
print(id(tom))
# lazy对象
lazy = Cat()
lazy.drink()
lazy.eat()
print(id(lazy))