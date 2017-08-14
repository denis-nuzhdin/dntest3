#глава №3, страница 103, игра Отгадай число, задание номер 4

import random

NUMBER_MIN = 1
NUMBER_MAX = 100
NUMBER = 1


#guess = int(input("num: "))
tires = 1


def ask_number(question):
    """просит ввести число из диапазона"""
    responce = None
    while responce not  in range(NUMBER_MIN,NUMBER_MAX):
        responce = int(input(question))
    return responce

guess = ask_number("Выбери число: ")


while NUMBER!= guess:
    if NUMBER > guess:
        print("less")
        NUMBER_MAX=NUMBER
    else:
        print("more")
        NUMBER_MIN=NUMBER
    NUMBER = int(random.randint(NUMBER_MIN, NUMBER_MAX))

    #guess = int(input("try again: "))
    tires += 1
    print(NUMBER)

    if NUMBER!=guess and tires >=5:
        print("looser")
        break
    elif NUMBER!=guess and tires<5:
        print("next numb")

    else:
        print("winner")
