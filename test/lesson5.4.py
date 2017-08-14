import random

list = ["111",
        "222",
        "333",
        "444",
        "555",
        "666",
        "777",
        "888",
        "999"]
list2 = list
new_list = []
weight = len(list)


for i in range(weight):
    weight = len(list2)
    new = random.choice(list)
    new_list.append(new)
    list2.remove(new)
print(new_list)