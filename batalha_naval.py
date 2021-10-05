# Projeto de jogo de batalha naval usando programação estruturada

# Flux conditions

win_condition = False
p_set = [False, False]
cont = False

# Ship dictionary

ship_dic = {'Carrier':[5,1], 'Battleship': [4,2], 'Cruiser': [3,3], 'Destroyer': [2,4]}
ship_kind = {1:'Carrier', 2:'Battleship', 3:'Cruiser', 4:'Destroyer'}

ships_to_place = [ship_dic, ship_dic]

ships_set = [{}, {}]

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
    cor_dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
    start_col_int = cor_dic[start_col]
    ship_size = ship_dic[ship][0]
    
    if (start_row < 1 or start_row > 10 or start_col_int < 1 or start_col_int > 10):
        cont = False
        print('Input ouf of bounds! Input correct starting points')
    
    elif (orientation == 'H'):
        if(start_col_int + ship_size - 1 > 10):
            cont = False
            print('Ship out of bounds. Insert again!')
        else:
            for i in range(start_col_int, start_col_int + ship_size):
                if grid_item[start_row][i] == '@':
                    for j in range(start_col_int, i):
                        grid_item[start_row][j] = '~'
                    print('Not possible, try again!')
                    break
                else:
                    grid_item[start_row][i] = '@'
                    
    elif (orientation == 'V'):
        if(start_row + ship_size - 1 > 10):
            cont = False
            print('Ship out of bounds. Insert again!')
        else:
            for i in range(start_row, start_row + ship_size):
                if grid_item[i][start_col_int] == '@':
                    cont = False
                    for j in range(start_row,i):
                        grid_item[j][start_col_int] = '~'
                    print('Not possible, try again!')
                    break
                else:
                    grid_item[i][start_col_int] = '@'


def player_set_loop(player):
    print('Player ' + str(player) + ', arrange your ships in the game board!\n')
    while not(p_set[player - 1]):
        print('Options remaining for player ' + str(player) + ': Kind of ship: [size, quantity] \n')
        print('Your options are: \n')
        print(ships_to_place[player - 1])
        ship_code = int(input('\nSelect your ship kind according to the options above. Type 1 for Carrier, 2 for Battleship, 3 for Cruiser, 4 for Destroyer\n'))
        grid_render(grid)
        ship_start_row = int(input('\nSelect your starting row according to the grid\n'))
        ship_start_col_raw = input('\nSelect your starting column according to the grid\n')
        ship_start_col_trim = ship_start_col_raw.upper()
        ship_orientation_raw = input('\n Set your ship orientation: type V for vertical ou H for horizontal\n')
        ship_orientation_trim = ship_orientation_raw.upper()
        ship_placer(grid_P1, ship_kind[ship_code], ship_start_row, ship_start_col_trim, ship_orientation_trim)
        grid_render(grid_P1)
        ships_to_place[player - 1][ship_kind[ship_code]][1] -= 1
        print(ships_to_place[player - 1])
        if ships_to_place[player - 1][ship_kind[ship_code]][1] == 0:
            ships_set[player - 1] = ships_to_place[player - 1].pop(ship_kind[ship_code])
            print(ships_set[player - 1])
            if len(ships_to_place[player - 1]) == 0:
                p_set[player - 1] = True


# Loop de jogo principal

print('Welcome to Battleship!!\n')

player_set_loop(1)
player_set_loop(2)




#grid_render(grid_P1)
#grid_render(grid_P2)

#ship_placer(grid_P1, 'Carrier', 1, 'D', 'V')
#grid_render(grid_P1)
#ship_placer(grid_P1, 'Cruiser', 1, 'B', 'H')
#grid_render(grid_P1)