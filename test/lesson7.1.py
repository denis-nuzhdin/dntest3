import pickle,shelve

varietey = ["огурцы", "помидоры","капуста"]
shape = ["целые","кубиками","соломкой"]
brand = ["Главпрадукт","Ашан","Магнит"]

f = open("pickles1.dat", "wb")

pickle.dump(varietey,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()

f = open("pickles1.dat", "rb")
varietey = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(varietey)
print(shape)
print(brand)

f.close()

s = shelve.open("pickles2.dat")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"] = ["Главпрадукт","Ашан","Магнит"]

s.sync()

print("торговые марки - ", s["brand"])
print("формы - ", s["shape"])
print("виды овощей - ", s["variety"])

s.close()