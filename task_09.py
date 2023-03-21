print('''
#1. Что выведет на экран следующий код? Попробуйте угадать, а затем запустите 
код и проверьте вашу догадку.
a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)
''')
a = abs(10) + abs(-10)
print(a)  # 20
b = abs(-10) + -10
print(b)  # 0

print('''
#2. Постарайтесь с помощью функций dir и help узнать, как можно разбить 
строку на отдельные слова, а затем напишите небольшую программу, 
которая печатает слова из следующей строки через одно, начиная с первого 
слова («этот»):
"этот если способ вы плохо это подходит читаете для что-то 
шифрования пошло важных не сообщений так"
''')
my_str = '''этот если способ вы плохо это подходит читаете для что-то 
шифрования пошло важных не сообщений так'''
# dir(my_str)
# help(str.split)
for i in range(0, len(my_str.split()), 2):
    print(my_str.split()[i])

print('''
#3. Напишите программу для копирования файла. (Подсказка: нужно открыть файл, 
который вы собираетесь скопировать, считать из него данные, создать 
новый файл-копию и записать туда считанные данные.) 
Проверьте результат работы программы, напечатав содержимое файла копии на экране.
''')

file_path = 'new.txt'
copy_path = 'copy_new.txt'
new_file = open(file_path)
text = new_file.read()
new_file = open(copy_path, 'w')
new_file.write(text)
new_file.close()
new_file = open(copy_path)
print(new_file.read())
new_file.close()
