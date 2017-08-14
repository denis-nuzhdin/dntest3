geek = {"404": "описание1",
        "401": "описание2",
        "403": "описание3"}

choice = None

while choice !=0:
    print("""
    Меню:
    0 - Выйти
    1 - Найти
    2 - Добавить
    3 - Изменить
    4 - Удалить
    """)
    choice = input("выбор: ")
    print()

    if choice=="0":
        print("goodbay")

    elif choice =="1":
        term = input("какой термин перевести: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "означает", definition)
        else:
            print("термин не знаком")

    elif choice =="2":
        term = input("какой термин добавить: ")
        if term not in geek:
            definition = input("введите новый термин: ")
            geek[term] = definition
        else:
            print("термин уже есть")

    elif choice=="3":
        term = input("изменить: ")
        if term in geek:
            definition = input("измените определение: ")
            geek[term] = definition
        else:
            print("нет такого термина")
    elif choice=="4":
        term = input("удалить: ")
        if term in geek:
            del geek[term]
        else:
            print("термина нет")
