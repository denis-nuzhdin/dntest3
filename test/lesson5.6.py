#Задание из главы №5 "Кто твой папа"

family = {"Олег": {"отец":"Александр", "дед":"Петр"},
          "Дмитрий":{"отец": "Михаил", "дед":"Степан"}
          }

choice=None
sun=""
father=""
grandfather=""

#sun = input("Имя: ")
#print(sun)
#print("Дед: ",family[sun]["дед"])
#print("Отец: ",family[sun]["отец"])


while choice !=0:
    print("""
    Меню:
    0 - Выйти
    1 - Найти отца и деда
    2 - Добавить новое поколение
    3 - Удалить поколение
    """)
    choice = input("выбор № в меню: ")

    if choice == "0":
        print("goodbay")

    elif choice == "1":
        sun = input("Введите имя сына для добавления: ")
        if sun in family:
            print("Имя отца:", family[sun]["отец"])
            print("Имя деда:", family[sun]["дед"])
        else:
            print("Нет такого имени")

    elif choice=="2":
        sun = input("Введите имя сына для удаления покаления: ")
        if sun not in family:
            father = input("Введите имя отца: ")
            grandfather = input("Введите имя деда: ")
            family[sun] = dict(отец=father, дед=grandfather )
            print(family)
        else:
            print("уже есть")

    elif choice=="3":
        sun = input("Введите имя сына: ")
        if sun in family:
            del family[sun]
            print(family)
        else:
            print("такого имени нет в списке")