def read_global():
    print("в области функции read_global() значение равно", value)

def shadow_global():
    value = -10
    print("в области функции shadow_global() значение равно", value)

def change_global():
    global value
    value = -20
    print("в области функции change_global() значение равно", value)

value = 10
read_global()
shadow_global()
change_global()