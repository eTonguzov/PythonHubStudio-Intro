# import os
#
# list_parts = []
#
# for adress, papka, file in os.walk('C:\\'):
#     for i in file:
#         full_path = os.path.join(adress, i)
#         list_parts.append(full_path)

# 'r' открыть для чтения(по умолчанию)
# 't' открыть в текстовом режиме(по умолчанию)
# 'w' открыть для записи, содержимое файла удаляется, если файла нет, создается новый
# 'a' открыть для дозаписи в конец файла, если файла нет, создатся новый
# 'b' отекрыть в бинарном режиме
# '+' открыть для чтения и записи 'r+', 'w+', 'a+'


r = open('text.txt', 'w' )
r.write('Stroka text')
r.close()