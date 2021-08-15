score1 = int(input('1 семестр '))
score2 = int(input('2 семестр '))

x = (score1 + score2)/2

if 90 <= x and 100 >= x:
    print(f'{x} - Ваш балл,скидка на обучение 50%')
elif 80 <= x and 89 >= x:
    print(f'{x} - Ваш балл, скидка на обучение 30%')
elif 70 <= x and 79 >= x:
    print(f'{x} - Ваш балл, скидка на обучение 10%')
elif 0 <= x and 69 >= x:
    print(f'{x} - Ваш балл, скидки на обучение нет!')     
else:
    print(f'{x} - Ваш балл, скидка на обучение 50%')