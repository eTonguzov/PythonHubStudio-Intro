z = {1,2,3,4,5}
x = {3,4,5,6,7}
z.add(5)#добавляем к множеству элемент
# z.discard(6)#удаляет элемент
# z.discard(7)#но если такого элемента не будет в множестве(ошибки не будет)
# z.remove(7)#этот метод тоже удаляет элемент, но если его нет в множестве, то возникает ошибка
# y = z.union(x)#объединяем два множества
# r = z.update(x)#добавили к множеству z + x
y = z.intersection(x)#проверка пересечений множества z и x(возвращает одинаковые эклкменты множеств)
e = z.difference(x)#показывает какие значения из множества z не всипечаются во множестве х




print(e)
