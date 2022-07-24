q = open("example.txt", encoding='utf-8')
r1 = q.read()
list_znk = ['(',')', '"', '\n']#список знаков которые мы хотим удалить
for i in list_znk:#проходимся циклом по переменной r1
    r1 = r1.replace(i, '')#заменяй
print(r1)#убрали все скобки и кавычки

r2 = r1.split()#разбили по разделителю(по умолчани пробел)
print(r2)

new_text = ' '.join(r2)#объеденили обратно. '_*_' - чем заполнить
print(new_text)