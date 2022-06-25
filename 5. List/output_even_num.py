n = list(range(10, 21))
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)#добавляем в конец нового списка i
        n.remove(i)#удаляем из списк n i-й элемент
else:
    print(m)
    print(n)