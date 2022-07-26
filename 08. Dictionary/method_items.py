price = {'meat': 3, 'bread' :1, "potato": 0.5, "water": 2}

new = {}
for key, value in price.items(): # метод Items возвращает список-представление вида (key, value)
    print(key)
    print(value)
    # new[value] = key # здесь мы меняем местами ключ на значение

print(new)
# print(price.keys())
