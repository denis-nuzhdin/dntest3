import random

class Critter(object):

    hungers = [0,1,2,3,4,5,6,7,8,9,10]
    boredoms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    def __init__(self,name, hunger = random.randint(0,5), boredom = random.randint(0,5)):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = "объект класса"
        rep +=   "имя:" + self.name +"; " \
               + "голод:" + str(self.hunger)  +"; "\
               + "скука:" + str(self.boredom) +"; "
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5<= unhappiness <=10:
            m = "неплохо"
        elif 11<=unhappiness<=15:
            m = "не очень"
        else:
            m = "ужастно"
        return m

    def talk(self):
        print("меня зовут: ", self.name, " я себя чувствую ", self.mood, "\n")
        self.__pass_time()
        #print(self.name)
        #print(self.hunger)
        #print(self.boredom)

    def eat(self, food=4):
        food = int(input("сколько еды? "))
        print("ммм спасибо")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        print(self.name)
        print(self.hunger)
        print(self.boredom)


    def play(self, fun=4):
        print("ураа")
        self.boredom -=fun
        if self.boredom < 0:
            self.boredom =0
        self.__pass_time()
        print(self.name)
        print(self.hunger)
        print(self.boredom)


def main():
    crit_list=[]

    while True:
        try:
            amount = int(input("Сколько зверей создать? "))
            break
        except ValueError:
            print("Введите число")

    for critt in range(amount):
        crit_name = input("введите имя: ")
        crit = Critter(crit_name)
        crit_list.append(crit)

    choice = None

    while choice !="0":
        print \
            ("""
            Моя зверушка
            0 - выход
            1 - узнать самочувствие
            2 - покормить
            3 - поиграть
            """)
        choice = input("ваш выбор: ")
        if choice =="0":
            print("goodbay")

        elif choice == "1":
            for crit in crit_list:
                crit.talk()

        elif choice == "2":
            crit.eat()

        elif choice == "3":
            crit.play()

        elif choice == "4":
            for crit in crit_list:
                print(str(crit))


        else:
            print("no choice")

main()