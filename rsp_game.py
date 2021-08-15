import random

lets_continue = True

while lets_continue:
    player_choice = input('Начните игру: [R/S/P]').lower() # R-камень,S-ножницы,P-бумага

    if player_choice not in ['r', 's', 'p']: 
        print('Incorrect input. Try again.')
        continue

    comp_choise  = random.choice(['r', 's', 'p'])

    print(f'Ввод соперника = {comp_choise}')

    winning_combinations = [('p', 'r'), ('r', 's'), ('s', 'p')]

    if player_choice == comp_choise:
        print('Ничья')
    elif (player_choice, comp_choise) in winning_combinations:
        print('Вы победили')    
    else:
        print('Вы проиграли')

    lets_continue = input('Продолжим? [y/n]').lower() == 'y'       
    