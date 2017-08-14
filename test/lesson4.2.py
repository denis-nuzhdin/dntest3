#отгадать слово по его длинне задание главы 4, стр.133 №4

import random

WORDS = ("apple", "google","help","house")

word = random.choice(WORDS)
trys = 3
correct=""
print(word)
print("Длинна слова:",len(word))

for l in range(trys):
    ll = input("Введите букву: ")
    print(ll)
    if ll in word:
        print("Yes")
    else:
        print("No")
correct = input("Введите слово: ")

if correct.lower()==word.lower():
    print("winer")
else:
    print("looser")



