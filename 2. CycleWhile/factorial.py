while True:#постонный цикл будет бесконечно просить ввод данных
    #расчитаем факториал числа x
    x = int(input())
    count = 0#счетчик
    y = 1#начальная переменная
    while(count<x): # здесь обозначили переменную count
        count+=1
        y *= count
    else:
        print(y)