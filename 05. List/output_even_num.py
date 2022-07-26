#нужно из списка чисел создать список с четными числами и оставить в старом списке только нечетные

old_list = list(range(1, 21))
#the_old_list = old_list.copy()# or the_old_list = old_list[start:stop:step] синтаксис срезов
the_old_list = old_list[1::2]
new_list = []
for i in old_list:
    if i % 2 == 0:
        new_list.append(i)#добавляем в конец нового списка i
        old_list.remove(i)#удаляем из списк n i-й элемент
else:
    print(new_list)
    print(old_list)
print(the_old_list)
