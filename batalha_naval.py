# Projeto de jogo de batalha naval usando programação estruturada

# Flux conditions

win_condition = False
p_set = [False, False]
cont = False

# Ship and grid dictionary

ship_dic = {'Carrier':[5,1], 'Battleship': [4,2], 'Cruiser': [3,3], 'Destroyer': [2,4]}
ship_kind = {1: 'Carrier', 2: 'Battleship', 3:'Cruiser', 4:'Destroyer'}
cor_dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}

ships_to_place = [ship_dic, ship_dic]

ships_set = [[], []]

# Grid initialization

grid = [['  ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        ['1 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['2 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['3 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['4 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['5 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['6 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['7 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['8 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['9 ','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
        ['10','~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

grid_P1 = grid
grid_P2 = grid
game_P1 = grid
game_P2 = grid

# Função de renderização
def grid_render(grid_item):
    for row in grid_item:
        print('\n')
        for element in row:
            print(element, end = '   ')
    print('\n')


# Função de posicionamento dos navios
def ship_placer(grid_item, ship, start_row, start_col, orientation):
    start_col_int = cor_dic[start_col]
    ship_size = 6 - ship
    locus = []
    
    if (start_row < 1 or start_row > 10 or start_col_int < 1 or start_col_int > 10):
        print('Input ouf of bounds! Input correct starting points')
        return None
    
    elif (orientation == 'H'):
        if(start_col_int + ship_size - 1 > 10):
            print('Ship out of bounds. Insert again!')
            return None
        else:
            for i in range(start_col_int, start_col_int + ship_size):
                if grid_item[start_row][i] == '@':
                    for j in range(start_col_int, i):
                        grid_item[start_row][j] = '~'
                    print('Not possible, try again!')
                    return None
                else:
                    grid_item[start_row][i] = '@'
                    locus.append([start_row, i])
            print(locus)
            return locus
                    
    elif (orientation == 'V'):
        if(start_row + ship_size - 1 > 10):
            print('Ship out of bounds. Insert again!')
            return None
        else:
            for i in range(start_row, start_row + ship_size):
                if grid_item[i][start_col_int] == '@':
                    for j in range(start_row,i):
                        grid_item[j][start_col_int] = '~'
                    print('Not possible, try again!')
                    return None
                else:
                    grid_item[i][start_col_int] = '@'
                    locus.append([i, start_col_int])
            print(locus)
            return locus


def player_set_loop(player):
    
    print('Player ' + str(player) + ', arrange your ships in the game board!\n')
    
    while ships_to_place[player - 1]:
        print('Options remaining for player ' + str(player) + ': Kind of ship: [size, quantity, option index] \n')
        print('Your options are: \n')
        print(ships_to_place[player - 1])
        
        ship_code = select_ship(ships_to_place[player - 1])
        grid_render(grid)
        row = select_row()
        col = select_column()
        orientation = select_orientation()
        ship_placed = ship_placer(grid_P1, ship_code, row, col, orientation)
        
        if  ship_placed is not None:
            ships_to_place[player - 1][ship_kind[ship_code]][1] -= 1
            ships_set[player - 1].append([ship_kind[ship_code], ship_placed])
        
        
        print(ships_set[player - 1])
        
        grid_render(grid_P1)
        
        if ships_to_place[player - 1][ship_kind[ship_code]][1] == 0:
            ships_to_place[player - 1].pop(ship_kind[ship_code])


def select_ship(ships_to_place):
    ship_code = 0
    choices = []
    for ship in ships_to_place:
        for key in ship_kind:
            if ship == ship_kind[key]:
                choices.append(key)
    while ship_code not in choices:
        print('Your available choices are: ')
        print(choices)
        ship_code = int(input('\nSelect your ship kind according to the options above. Type 1 for Carrier, 2 for Battleship, 3 for Cruiser, 4 for Destroyer\n'))
    return ship_code

def select_row():
    row = 0
    choices = list(range(1,11))
    while row not in choices:
        row = int(input('\nSelect your starting row according to the grid\n'))
    return row

def select_column():
    col = 0
    choices = ['A','B','C','D','E','F','G','H','I','J']
    while col not in choices:
        col = input('\nSelect your starting column according to the grid\n').upper()
    return col

def select_orientation():
    orientation = ''
    choices = ['V','H']
    while orientation not in choices:
        orientation = input('Set your ship orientation: type V for vertical ou H for horizontal\n').upper()
    return orientation

def attack_loop():
    
    while (ships_set[0] is not None) and (ships_set[1] is not None):
        x_p1 = int()


# Loop de jogo principal
print('\n=======================')
print('Welcome to Battleship!!')
print('=======================\n')

player_set_loop(1)
player_set_loop(2)



#grid_render(grid_P1)
#grid_render(grid_P2)

#ship_placer(grid_P1, 'Carrier', 1, 'D', 'V')
#grid_render(grid_P1)
#ship_placer(grid_P1, 'Cruiser', 1, 'B', 'H')
#grid_render(grid_P1)