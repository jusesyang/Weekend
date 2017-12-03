
class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print("%s is talking"%self.name)


class Man(People):
    def __init__(self,name,age,money):
        super(Man,self).__init__(name,age,money)
        self.money = money

    def talk(self):
        # super(Man,self).talk()
        print("%s %s have $%s money"%(self.name,self.age,self.money))

m1=Man("yang",26,"100")
m1.talk()



