# анограмма, угадывание слов по буквам в перемешку, глава 4

import random

WORDS = ("home",
             "python",
             "apple",
             "google",
             "led zeppelin",
             "lp")

word = random.choice(WORDS)
correct = word

jumble =""

while word:
    position = random.randrange(len(word))
    #print("position: ",position)
    jumble += word[position]
    word = word[:position] + word[(position+1):]
    #print("word: ", word)
    #print("jumble: ", jumble)

print("anogram",jumble)
guess = input("what? ")

helps = ("hepl1", "help1", "help3")
point = 5

while guess !=correct and guess!="":
    #print("again!")
    help = input("can i help you? ")
    if help == "yes":
        print(random.choice(helps))
        guess = input("try with help: ")
        point=1
    elif help =="no":
        guess = input("try: ")
        point=2
    else:
        break

if guess==correct:

    print("win! and point ",point)
