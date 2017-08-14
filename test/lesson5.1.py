scores = []
choice = None

while choice !="0":
    print("""
    Рекорды:
    0 - выйти
    1 - показать рекорды
    2 - добавить рекорд
    """)
    choice = input("выбор: ")
    print()

    if choice =="0":
        print("goodbay")

    elif choice =="1":
        print("Рекорды список:\n")
        print("Name\tResult")
        for entry in scores:
            score,name = entry
            print(name,"\t",score)


    elif choice=="2":
        name = input("Введите имя: ")
        score = int(input("Введите рекорд: "))
        entry = (score,name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores=scores[:5]


    else:
        print("Нет такого пункта")

