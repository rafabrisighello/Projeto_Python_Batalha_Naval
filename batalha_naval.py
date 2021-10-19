# Battleship terminal game project - Rafael Brisighello

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

grids = [grid,grid]

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
    
    print('Player ' + str(player) + ', arrange your ships in the game board!')
    
    print(ships_to_place)

    while ships_to_place[player - 1]:
        
        grid_render(grids[player - 1])
        print('Options remaining for player ' + str(player) + ': Kind of ship: [size, quantity] \n')
        print('Your options are: \n')
        print(ships_to_place[player - 1])
        
        ship_code = select_ship(ships_to_place[player - 1])
        row = select_row()
        col = select_column()
        orientation = select_orientation()
        ship_placed = ship_placer(grids[player - 1], ship_code, row, col, orientation)
        
        if  ship_placed is not None:
            ships_to_place[player - 1][ship_kind[ship_code]][1] -= 1
            ships_set[player - 1].append([ship_kind[ship_code], ship_placed])
        
        print(ships_set[player - 1])      
        
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

def attack_loop(player):
    
    r_P = int(input("\n P{0}, choose row coordinate to bomb: ".format(player - 1)))
    cint_P = int(input("\n P{0}, choose clumn coordinate to bomb: ".format(player - 1)))
    c_P = cor_dic(cint_P)
    attack_point = [r_P, c_P]
    rival = 0
    
    if player == 1:
        rival == 2
    else:
        rival == 1

    for ship in ships_set[rival - 1]:
        for coordinates in ship[1]:
            if (r_P == coordinates[0]) and (c_P == coordinates[1]):
                grids[player - 1][r_P][c_P] = 'X'
                coordinates.pop()
                print("\n P{0}'s ship hit!!! It was a {1}!!!".format(rival, ship[0]))
                grid_render(grids[player - 1])
                if len(ship[1]) == 0:
                    print("\n P{0}'s ship sunk!!! It was a {1}!!!".format(rival, ship[0]))
                    ships_set[player - 1].pop(ship)
                    if len(ship) == 0:
                        return True
            return False   
    return False

def main_loop():
    
    end_condition = False
    play_count = 1
    while end_condition != True:
        if (play_count % 2) != 0:
            end_condition = attack_loop(1)
            winner = 1
        else:
            end_condition = attack_loop(2)
            winner = 2
        play_count += 1

    print("P{0} wins!!!!! Congratulations!!!!".format(winner))

def game():
    # Welcome
    print('\n==============================================')
    print('!!!           Welcome to Battleship          !!!')
    print('==============================================\n')
    
    # Board Setting Loop
    player_set_loop(1)
    player_set_loop(2)

    # Attack Loop
    main_loop()

game()


