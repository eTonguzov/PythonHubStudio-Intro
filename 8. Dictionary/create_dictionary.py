d0 = {}#пустой словарь
d1 = {"a":7}#здесь а-это ключ, 7 - значение
d2 = dict(a=7)#подается именнованный аргумент
d3 = dict.fromkeys([1, 2, 3, 4, 5], 'value')# позволяет создать словарь состоящий из ключей состоящих из значений по умолчанию(по умолчанию это None)
print(d1)
print(d3)

# Зачем нужен словарь
price = {"meat":3, "bread":1, "potato":0.5, "water": 2} #может иметь любой неизменяемый тип данных

def pay():
    pay = 0
    while True:
        enter = input('Что покупаем?\n')
        if enter == 'end':
            break
        pay += price[enter]
    return pay
# pay()
#  глобальный словарь
users = {
    'Egor': {'password': 90009090, 'id': 19090},
    'Jimmy': {'password': 434345353, 'id': 554455}
    }


