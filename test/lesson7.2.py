import sys

def open_file(file_name,mode):
    """открываем файл"""
    try:
        the_file = open(file_name,mode,encoding='utf-8')
    except IOError as e:
        print("Не возможно открыть файл: ", file_name)
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """возвращает в форматироанном виде строку"""
    line = the_file.readline()
    line.replace("/","\n")
    return line

def next_block(the_file):
    """возвращает блок данных"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    weight = next_line(the_file)
    correct = next_line(the_file)

    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, weight, correct, explanation

def welcome(title):
    print("Добро пожаловать")
    print("\t\t", title, "\n")

def player_name():
    name_player = input("введите имя: ")
    return name_player


def main():
    record = []
    name = player_name()
    trivia_file = open("trivia.txt","r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    category, question, answers,weight, correct, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        answer = input("ваш ответ:")

        if answer == correct:
            print("\n Да", end=" ")
            score += int(weight)
        else:
            print("\n Нет", end=" ")
        print(explanation)
        print("Счет: ", score, "\n")

        #переход к следующему вопросу
        category, question, answers, weight, correct, explanation = next_block(trivia_file)

    trivia_file.close()
    print("конец")
    print(name, "ваш счет: ", score)
    record.append(name,)
    record.append(str(score))

    print(record)

    save_record = open("record.txt", "a", encoding="utf-8")
    #save_record.writelines(record)
    save_record.write(name)
    save_record.write("\t")
    save_record.write(str(score))
    save_record.writelines("\n")
    save_record.close()

main()