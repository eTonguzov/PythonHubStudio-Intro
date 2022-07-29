#парсинг файлов
import sys

url_list = ['text.txt', 'text2.txt', 'text25.txt', 'text3.txt']

list_defect = []
list_info = []

try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())
            print('Открылся без ошибки')

        except Exception:# Exception - группа ошибок
            list_defect.append(url)
            print('Ошибка типа Exeption')
            sys.exit()#здесь мы вызвали экстренное завершение прграммы(генерация ошибки)
            continue
finally:# сохраним данные при экстренном зкрытии программы(даже при генерации ошибки)
    r = open('save.txt', 'a')# открываем текстовый документ(save.txt)# 'a' - открыть для дозаписи в конец файла, если файла нет, создатся новый
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print("Я все записал несмотря ни на что")
#
#
print(list_defect)
print(list_info)