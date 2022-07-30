import newmod as nm# импортируй модуль newmod как nm(любое имя)

k = 1#переменная в этой программе
print(k)
nm.k = 8#переменная в из модуля newmod
print(nm.k)
# print(newmod.newf(3))#передали на вход функции(3)
# print(dir(nm))
# print(help(nm))#справка по модулю newmod

print(nm.__name__)# тк. == newmod поэтому здесь мы не можем запустить "Введите число из модуля"

