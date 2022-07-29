while True:
    try:
        enter = float(input("Введите число "))
        print(100/enter)
        # break
    except ValueError:
        print("выввели не число")#перехватит ошибку и исполнит тот код который мы пропишем в этом блоке кода
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
    else:
        print("Пользователь молодец, с первого раза")
    finally:#исполняется всегда, то есть обрабатывает любую ошибку
        
        print("Я finally, я исполняюсь всегда! ")
print('Все норм')
