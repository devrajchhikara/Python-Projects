import random

def start():

    matrix = []

    for i in range(4):
        matrix.append([0]*4)

    print("Commands are as follows: \n1)'W' or 'w' to move upward\n2)'S' or 's' to move downward\n3)'A' or 'a' to move left\n4)'S' or 's' to move right\n")

    add_new_2(matrix)
    return matrix

def add_new_2(matrix):

    r = random.randint(0,3)
    c = random.randint(0,3)

    while (matrix[r] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)

    matrix[r] = 2


def get_current_state(matrix):

    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 2048):
                    return "You Won"
            
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 0):
                return "Game not over"
    
    for i in range(3):
        for j in range(3):
            if ( matrix[i][j] == matrix[i+1][j] or matrix[i][j] == matrix[i][j+1] ):
                return "Game not over"
            
    for j in range(3):
        if (matrix[3][j] == matrix[3][j+1]):
            return "Game not over"
    
    for i in range(3):
        if (matrix[i][3] == matrix[i+1][3]):
            return "Game not over"
        
    return "Lost"

def compress(matrix):

    changed = False

    new_mat = []

    for i in range(4):
        new_mat.append([0]*4)

    for i in range(4):
        pos = 0

        for j in range(4):
            if(matrix[i][j] != 0):

                new_mat[i][pos] = matrix[i][j]
                 
                if(j != pos):
                    changed = True
                pos += 1
    return new_mat, changed

def merge(matrix):

    changed = False

    for i in range(4):
        for j in range(4):


            if (matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0):

                matrix[i][j] = matrix[i][j]*2
                matrix[i][j+1] = 0 

                changed = True
    return matrix, changed

def reverse(matrix):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(matrix[i][3-j])
    return new_mat


def transpose(matrix):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(matrix[j][i])
    return new_mat




def move_left(grid):
    new_grid, changed1 = compress(grid)

    new_grid, changed2 = merge(new_grid)

    changed = changed1 or changed2

    new_grid, temp = compress(new_grid)

    return new_grid, changed

def move_right(grid):

    new_grid = reverse(grid)

    new_grid, changed = move_left(new_grid)

    new_grid = reverse(new_grid)

    return new_grid, changed

def move_up(grid):

    new_grid = transpose(grid)

    new_grid, changed = move_left(new_grid)

    new_grid = transpose(new_grid)

    return new_grid, changed

def move_down(grid):

    new_grid = transpose(grid)

    new_grid, changed = move_right(new_grid)

    new_grid = transpose(new_grid)

    return new_grid, changed

     