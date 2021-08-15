val_1 = int(input('Введите число '))
val_2 = int(input('Введите число '))
oper = input('Сложение или вычитание ')
total_sum = val_1 + val_2
total_sub = val_1 - val_2
if oper == '+':
    print(f'Сумма {total_sum}')
elif oper == '-':
    print(f'Разность {total_sub}')
else:
    print('Еще раз')