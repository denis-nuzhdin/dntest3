
class Critter(object):
    def __init__(self,name):
        print("появиась новая зверушка")
        self.name = name

    def __str__(self):
        rep = "Объект класса\n"
        rep += "имя" + self.name + "\n"
        return rep

    def talk(self):
        print("Привет",self.name,"\n")

crit1 = Critter("bob")
crit1.talk()
crit2 = Critter("mike")
crit2.talk()

print("вывод объекта: ")
print(crit1)
print("доступ к: ")
print(crit1.name)