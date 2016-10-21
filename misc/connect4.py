def create_dict():

    return {
        'left': 4,
        'right':4,
        'down': 4,
        'up': 4,
        'upper_right': 4,
        'upper_left': 4,
        'lower_right': 4,
        'lower_left':4
    }

def valid_point(x,y, row_limit, column_limit):

    return  0 <= x < row_limit and y <= 0 < column_limit

def return_points(i,j):
    """
    up = (i, j + 1)
    down = (i, j - 1)
    left = (i, j + 1)
    right = (i, j + 1)
    upper_right = (i, j + 1)
    upper_left = (i, j + 1)
    lower_right = (i, j + 1)
    lower_left = (i, j + 1)
    """
    return ((i, j + 1)
    (i, j - 1),
    (i, j + 1),
    (i, j + 1),
    (i, j + 1),
    (i, j + 1),
    (i, j + 1),
    (i, j + 1))



def solve(board):

    rows = len(board)
    cols = len(board[0])

    def valid_point(x,y):
        return valid_point(x,y, rows, cols)

    def search(index_to_search, seen_already, came_from, expecting):

        seen_already.add(index_to_search)

        i,j = index_to_search



        for coord in (up, down, left, upper_right, upper_left,lower_right, lower_left):












R, B= 'R','B'
i = [
     [R,R,R,B,R],
     [R,B,B,R,B],
     [R,B,R,B,R]
     [R,B,R,B,R]
]
