x = 5#глобальная переменная

def name():
    #global x #ключевое слово global означат что мы хотим внести изменения в глобальную прерменную x(global)
    x = 100#локальная переменная
    return name2(x)

def name2(par):
    print(par)
name()