import  random

HANGMAN = ("kill 1",
           "kill 2",
           "kill 3",
           "kill 4",
           "kill 5",
           "kill 6",
           "kill 7",
           "kill 8")

MAX_WRONG = len(HANGMAN)-1
WORDS = ("APPLE",
         "GOOGLE",
         "AMAZON",
         "INTEL")

word = random.choice(WORDS)
print(word)
so_far = "-" * len(word)
wrong = 0
used = []

while wrong < MAX_WRONG and so_far!=word:
    print(HANGMAN[wrong])
    print("вы предлагали буквы: \n", used)
    print("отгаданное слово: \n", so_far)

    guess = input("введите букву: ")
    guess = guess.upper()

    while guess in used:
        print("вы предлагали букву:", guess)
        guess = input("букву: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("такая буква есть")
        new =""
        for i in range(len(word)):
            if guess == word[i]:
                new +=guess
            else:
                new+=so_far[i]
        so_far = new

    else:
        print("нет такой буквы")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("game over")

else:
    print("winn!")
print(word)