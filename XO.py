def print_desk(game_desk):
    print(*[i for i in game_desk], sep='\n')


def is_valid(y, x, game_desk, sign):
    flag = True
    while flag:
        if game_desk[y][x] == '*':
            game_desk[y][x] = sign
            flag = False
        else:
            print('поле занято, попробуйте в другую клетку')
            y = int(input('Введите y координат'))
            x = int(input('Введите х координат'))

    # X valid
    if game_desk[0][0] == 'X' and game_desk[0][1] == 'X' and game_desk[0][2] == 'X':
        return 'Победили X'
    elif game_desk[0][0] == 'X' and game_desk[1][0] == 'X' and game_desk[2][0] == 'X':
        return 'Победили X'
    elif game_desk[0][0] == 'X' and game_desk[1][1] == 'X' and game_desk[2][2] == 'X':
        return 'Победили X'
    elif game_desk[0][1] == 'X' and game_desk[1][1] == 'X' and game_desk[2][1] == 'X':
        return 'Победили X'
    elif game_desk[0][2] == 'X' and game_desk[1][2] == 'X' and game_desk[2][2] == 'X':
        return 'Победили X'
    elif game_desk[0][2] == 'X' and game_desk[1][1] == 'X' and game_desk[2][0] == 'X':
        return 'Победили X'
    elif game_desk[1][0] == 'X' and game_desk[1][1] == 'X' and game_desk[1][2] == 'X':
        return 'Победили X'
    elif game_desk[2][0] == 'X' and game_desk[2][1] == 'X' and game_desk[2][2] == 'X':
        return 'Победили X'

    # 0 valid
    if game_desk[0][0] == '0' and game_desk[0][1] == '0' and game_desk[0][2] == '0':
        return 'Победили 0'
    elif game_desk[0][0] == '0' and game_desk[1][0] == '0' and game_desk[2][0] == '0':
        return 'Победили 0'
    elif game_desk[0][0] == '0' and game_desk[1][1] == '0' and game_desk[2][2] == '0':
        return 'Победили 0'
    elif game_desk[0][1] == '0' and game_desk[1][1] == '0' and game_desk[2][1] == '0':
        return 'Победили 0'
    elif game_desk[0][2] == '0' and game_desk[1][2] == '0' and game_desk[2][2] == '0':
        return 'Победили 0'
    elif game_desk[0][2] == '0' and game_desk[1][1] == '0' and game_desk[2][0] == '0':
        return 'Победили 0'
    elif game_desk[1][0] == '0' and game_desk[1][1] == '0' and game_desk[1][2] == '0':
        return 'Победили 0'
    elif game_desk[2][0] == '0' and game_desk[2][1] == '0' and game_desk[2][2] == '0':
        return 'Победили 0'
        
    return game_desk


desk = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
s = ''

print_desk(desk)

for i in range(9):
    if i % 2 == 0:
        print('Player 1')
        s = '0'
        coord_y = int(input('Введите y координат'))
        coord_x = int(input('Введите х координат'))
        desk = is_valid(coord_y, coord_x, desk, s)
        print_desk(desk)
    else:
        print('Player 2')
        s = 'X'
        coord_y = int(input('Введите y координат'))
        coord_x = int(input('Введите х координат'))
        desk = is_valid(coord_y, coord_x, desk, s)
        print_desk(desk)