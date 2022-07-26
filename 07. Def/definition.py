def counter(par, par2 = False, count =0):#здесь count и par2 это параметры по умолчанию(записывается всегда последним)
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ

    else:
        for i in par:
            count+=1
        return count

j = [3, 4, 5, 9]
h = ["ff", "yy", "ii"]
k = [4, 5,2,322, 33]

print(counter(j))
print(counter(j, True, -1))
x, y = counter(j, True, -1)#распаковка
print(x, y,)
# print(counter(k))
# print((counter("string")))