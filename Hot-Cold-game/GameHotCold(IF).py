import random
razn = 0
print("Введи читсло от 1 до 10")
rand_num = random.randint(1,10)#Генерируем числа от 1 до 10
# print(rand_num)
my_num = int(input())# Вводим свое число
# print(my_num, rand_num)
if(my_num==rand_num):
    print("Угадал")
elif(my_num>rand_num):
    razn = my_num-rand_num
else: razn = rand_num - my_num
# print(razn)

if(razn>=3):
    print("Холодно, попробуй заново:")
    new_my_num = int(input())
    if(new_my_num==rand_num):
        print("Даа, ты угадал")
    else: print("Неверно, извини попыток брольше нет")# здесь нужно реализовать завершение программы
if (razn == 2):
        print("Прохладно, попробуй заново:")
        new_my_num = int(input())
        if (new_my_num == rand_num):
            print("Даа, ты угадал")
        else:
            print("Неверно, извини попыток брольше нет")  # здесь нужно реализовать завершение программы
if (razn == 1):
        print("Горячо, попробуй заново:")
        new_my_num = int(input())
        if (new_my_num == rand_num):
            print("Даа, ты угадал")
        else:
            print("Извини попыток брольше нет")  # здесь нужно реализовать завершение программы