print('''
Решите эти задачи, используя конструкции if и условия.

1. Вы богаты?
''')
money = 2000
dream_money = 1000
if money > dream_money:
    print("Я богат!")
else:
    print("Я не богат!")
    print("Может, когда-нибудь потом…")

print('''
2. Бисквитики!

  Создайте конструкцию if, которая проверяет, действительно ли количество 
  бисквитов (которое задано в переменной twinkies) меньше 100 
  или больше 500. Если это условие выполняется, пусть ваша программа 
  напечатает сообщение «Слишком мало или слишком много»
  ''')
twinkies = 700
min = 100
max = 500
if twinkies < min:
    print('Слишком мало бисквитов')
elif twinkies > max:
    print('Cлишком много бисквитов')

print('''
3. Подходящая сумма

  Создайте конструкцию if, которая проверяет, соответствует ли заданная в 
  переменной money сумма денег диапазону значений от 100 до 500 
  или диапазону значений от 1000 до 5000.
''')
money = 60
min_1 = 100
max_1 = 500
min_2 = 1000
max_2 = 5000
if money >= min_1 and money <= max_1:
    print('Входит в первый диапазон')
elif money >= min_2 and money <= max_2:
    print('Входит во второй диапазон')
else:
    print('Не входит в диапазоны')

print('''
4. Я одолею этих ниндзя!

  Создайте конструкцию if, которая печатает строку «Их слишком много», 
  если количество ниндзя (заданное в переменной ninjas) меньше 50, 
  печатает «Будет непросто, но я с ними разделаюсь», если это количество 
  меньше 30, и печатает «Я одолею этих ниндзя!», если количество меньше 10. 
  Проверьте, как ваш код работает с таким значением: ninjas = 5
  ''')
ninjas = 50
if ninjas < 10:
    print('Я одолею этих ниндзя!')
elif ninjas < 30:
    print('Будет непросто, но я с ними разделаюсь')
elif ninjas < 50:
    print('Их слишком много')
else:
    print('NinjAпокалипсис')
