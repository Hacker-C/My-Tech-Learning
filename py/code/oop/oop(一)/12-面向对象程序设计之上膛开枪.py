class Gun:

    def __init__(self, model):
        self.bullet_count = 0
        self.model = model

    def shoot(self):
        if self.bullet_count <= 0:
            print("[{}]没子弹啦！[0]".format(self.model))
            return
        self.bullet_count -= 1
        print('[{}]突突突...[子弹剩余{}]'.format(self.model, self.bullet_count))

    def add_bullet(self, count):
        self.bullet_count += count
        # print("[{}]颗子弹已上膛！[共{}颗子弹]".format(count, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("[{}]还没有枪...".format(self.name))
            return
        print("冲啊...[{}]".format(self.name))

        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun('ak47')
xusanduo = Soldier('许三多')
xusanduo.gun = ak47
xusanduo.fire()
