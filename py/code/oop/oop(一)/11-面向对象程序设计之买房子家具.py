class HouseItem:

    def __init__(self, name, area) -> None:
        self.name = name
        self.area = area

    def __str__(self) -> str:
        return "[{}]占地{}".format(self.name, self.area)


bed = HouseItem('席梦思', 40)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)


class House:

    def __init__(self, house_type, area) -> None:
        self.houese_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def add_item(self, house_item) -> None:
        if house_item.area > self.free_area:
            print('[{}]已经放不下了。'.format(self.houese_type))
        else:
            self.item_list.append(house_item.name)
            self.free_area -= house_item.area

    def __str__(self) -> str:
        return ("{}\n户型：{}\n总面积：{}\n剩余面积：{}\n家具：{}\n{}".format(
            '-' * 30,
            self.houese_type, self.area,
            self.free_area, self.item_list,
            '-' * 30))


my_home = House('两室一厅', 100)
print(my_home)
my_home.add_item(bed)
my_home.add_item(chest)
print(my_home)
my_home.add_item(bed)
my_home.add_item(bed)
print(my_home)