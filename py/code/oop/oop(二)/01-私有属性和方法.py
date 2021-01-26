class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("{}的年龄是{}".format(self.name, self.__age))

    def f(self):
        print(self.__age)

xiaohua= Women('小花')
print(xiaohua._Women__age)
