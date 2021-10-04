# Projeto de jogo de batalha naval usando programação estruturada

print('Welcome to Battleship!!')

win_condition = False

ship_dic = {'Carrier':[5, 1], 'Battleship': [4,2], 'Cruiser': [3,3], 'Destroyer': [2,4]}

grid = [['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]


def grid_render(grid_item):
    for row in grid_item:
        print('\n')
        for element in row:
            print(element, end = '   ')
    print('\n')


grid_P1 = grid
grid_P2 = grid

grid_render(grid_P1)
grid_render(grid_P2)