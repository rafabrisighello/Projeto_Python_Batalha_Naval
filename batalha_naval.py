# Projeto de jogo de batalha naval usando programação estruturada

print('Welcome to Battleship!!')

win_condition = False

ship_dic = {'Carrier':[5, 1], 'Battleship': [4,2], 'Cruiser': [3,3], 'Destroyer': [2,4]}

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

#Função de renderização
def grid_render(grid_item):
    for row in grid_item:
        print('\n')
        for element in row:
            print(element, end = '   ')
    print('\n')


# Função de posicionamento dos navios
def ship_placer(grid_item, ship, start_row, start_col, orientation):
    cor_dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
    start_col_int = cor_dic(start_col)
    ship_size = ship_dic[ship][0]
    if (start_row < 1 or start_row > 10 or start_col_int < 1 or start_col_int > 10):
        return 'Input ouf of bounds! Input correct starting points'
    elif ((orientation == 'H' and start_row + ship_size > 10) or (orientation == 'V' and start_col + ship_size > 10)):
        return 'Ship out of bounds. Insert again'


grid_P1 = grid
grid_P2 = grid

grid_render(grid_P1)
grid_render(grid_P2)
