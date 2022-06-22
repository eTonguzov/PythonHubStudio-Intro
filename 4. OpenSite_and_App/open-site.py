import os # импорт модуля OS
while True:
    site = input("Введите адрес сайта\n")
    if (site == "завершить"):
        break

    if "https://" in site:#здесь оператор in проверяет есть ли в последо-ти другая последов-ть
        os.system("start " + site)
        #print("if")

    elif "www." in site:
        site = "https://" +  site
        os.system("start " + site)
        #print("elif")
    else:
        site = "https://www." + site
        os.system("start " + site)
        #print("else")