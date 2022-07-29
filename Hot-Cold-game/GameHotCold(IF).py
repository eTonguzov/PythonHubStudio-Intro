import random

print("Привет, давай поиграем в игру!\nЯ загадаю число от [0 до 10] И ты попытаешься его угадать")

def get_user_num():
    while True:
        try:
            user_num = int(input("Введи целое (int) число которое ты загадал\n"))

        except ValueError:
            print("Извини, так не пойдет, введи заново")


        if user_num<0:
            print("Вы ввели отрицательное число")
            continue
        else:
            break
    return user_num

ran_num = random.randint(0,10)
get_user_num()
print(get_user_num())



# count_try = 10
# print('У тебя будет', count_try, 'попыток')
# while count_try>0:
#     while count_try!=ran_num:
#         if count_try>ran_num:
#             razn = count_try-ran_num
#             if razn > 3:
#                 print("Холодно")
#             elif razn==2:
#                 print('Тепло')
#             else: print("Горячо")
#         if count_try<ran_num:
#             razn = ran_num-count_try
#             if razn > 3:
#                 print("Холодно")
#             elif razn==2:
#                 print('Тепло')
#             else: print("Горячо")


print(ran_num)