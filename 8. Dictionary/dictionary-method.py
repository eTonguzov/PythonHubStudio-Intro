d1 = {'a': 7, 'b':9}
d2 = dict([[1,2], [3,4], [5,6]])
d3 = dict.fromkeys([1,2,3,4,5], 'value')

d1.clear() #очищает словарь
d5 = d1.copy() #позволяет скопировать словарь в новую переменную
print(d1.items()) #возврвщает список из кортежей
print(d1.keys()) #возвращает список из ключей словоря
print(d1.values()) #возвращает значение соловоря в ввиде списка
d1.update(d2) #позволяет добавить добавить значение прары ключа из одного словоря в другой
print(d1)

# метод Get
if 'c' in d1:
    d1['c']#только в этом случае запрашивай значение C из словоря
y = d1.get('c') #если в словоре будет значение С, то метод Get вернет это значение в пременную Y
print(y)

# метод Pop

t = d1.pop('a') # удаляет пару ключ-значение, и возвращает значение в пременную
print(t, d1)# 7 {'b': 9} Здесь показана работа метода Pop, ключ-значение a - 7 удалено, значение записанно в переменную t, осталась только пара b-9
