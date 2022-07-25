#%s, .format, f-строка.

enter = input("Your name: ")
s = 'Hello %s, I am %s' % (enter, 'Python')# старый способ форматирования строк

print(s)

s1 = 'Hello {1}, I am {0}'.format(enter, 'Python')

print(s1)

var = 'stroka'
s2 = f'Hello {enter}, I can do it in f-string {len(var)}'

print(s2)