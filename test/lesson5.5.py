#задание для главы 5, Генератор персонажей

points = 30

choice = None

strange = 0
health = 0
wisdom = 0
flex = 0

while choice !=0:
    print("""
    Меню:
    0 - Выйти
    1 - Добавить очки
    2 - Удалить очки
    3 - Посмотреть очки
    """)
    choice = input("выбор № в меню: ")

    if choice == "0":
        print("goodbay")

    elif choice == "1":
        skill = input("Куда начислить очки? Сила, Здоровье, Мудрость, Ловкость: ")
        if skill == "Сила":
            new_point = int(input("Количество очков: "))
            if new_point > points:
                print("Доступно только", points, "очков")
                new_point = int(input("Введите еще раз: "))
            strange += new_point
            points -= new_point

        elif skill == "Здоровье":
            new_point = int(input("Количество очков: "))
            if new_point > points:
                print("Доступно только", points, "очков")
                new_point = int(input("Введите еще раз: "))
            health += new_point
            points -= new_point

        elif skill == "Мудрость":
            new_point = int(input("Количество очков: "))
            if new_point > points:
                print("Доступно только", points, "очков")
                new_point = int(input("Введите еще раз: "))
            wisdom += new_point
            points -= new_point

        elif skill == "Ловкость":
            new_point = int(input("Количество очков: "))
            if new_point > points:
                print("Доступно только", points, "очков")
                new_point = int(input("Введите еще раз: "))
            flex += new_point
            points -= new_point

    elif choice == "2":
        skill = input("Откуда убрать очки? Сила, Здоровье, Мудрость, Ловкость: ")
        if skill == "Сила":
            new_point = int(input("Количество очков: "))
            if new_point > strange:
                print("Доступно только", strange, "очков для снятия")
                new_point = int(input("Введите еще раз: "))
            strange -= new_point
            points += new_point

        elif skill == "Здоровье":
            new_point = int(input("Количество очков: "))
            if new_point > health:
                print("Доступно только", health, "очков")
                new_point = int(input("Введите еще раз: "))
            health -= new_point
            points += new_point

        elif skill == "Мудрость":
            new_point = int(input("Количество очков: "))
            if new_point > wisdom:
                print("Доступно только", wisdom, "очков")
                new_point = int(input("Введите еще раз: "))
            wisdom -= new_point
            points += new_point

        elif skill == "Ловкость":
            new_point = int(input("Количество очков: "))
            if new_point > flex:
                print("Доступно только", flex, "очков")
                new_point = int(input("Введите еще раз: "))
            flex -= new_point
            points += new_point

    else:
        print("Нет такого пункта")
        break


    print("Очков:", points)
    print("Сила: ", strange)
    print("Здоровье: ", health)
    print("Мудрость: ", wisdom)
    print("Ловкость: ", flex)


