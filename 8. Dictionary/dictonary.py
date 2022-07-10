price = {'meat': 3, 'bread' :1, "potato": 0.5, "water": 2}
new_price = {}
for i in price:
    new_price =  round(price[i] * 0.85, 2) # встроенная функция round принимает на вход два аргумента. Число которое нужно округлить, и второй аргумент сколько знаков после запятой


print(price)
print(new_price)

x = price.items()
print(x)