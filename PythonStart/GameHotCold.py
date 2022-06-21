import random

print("Загадай число от 1 до 100, и я попробую отгадать его, введи его ниже")
rand_num = random.randint(1,100)
you_number = int(input())
# print(you_number)
#print(rand_num)
if rand_num==you_number:
    print("Ты победил!")
elif rand_num > you_number:
    num = rand_num-you_number
    if num >= 30:
        print("Северный полюс")
    elif num >=20 & num < 30:
        print("Холодно")
    elif num >=10 & num <20:
        print("Тепло")
    else:
        print("Горячо")
