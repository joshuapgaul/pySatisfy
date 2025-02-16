from toy_circuits import sudoku


def test_get_squares_by_column():
    cases = [ 
        (0, [0,9,18,27,36,45,54,63,72]),
        (1, [1,10,19,28,37,46,55,64,73]),
        (2, [2,11,20,29,38,47,56,65,74]),
        (3, [3,12,21,30,39,48,57,66,75]),
        (4, [4,13,22,31,40,49,58,67,76]),
        (5, [5,14,23,32,41,50,59,68,77]),
        (6, [6,15,24,33,42,51,60,69,78]),
        (7, [7,16,25,34,43,52,61,70,79]),
        (8, [8,17,26,35,44,53,62,71,80])
    ]

    for column_number, squares in cases:
        assert sudoku.get_squares_by_column(column_number) == squares

def test_get_squares_by_row():
    cases = [
        (0, [0,1,2,3,4,5,6,7,8]),
        (1, [9,10,11,12,13,14,15,16,17]),
        (2, [18,19,20,21,22,23,24,25,26]),
        (3, [27,28,29,30,31,32,33,34,35]),
        (4, [36,37,38,39,40,41,42,43,44]),
        (5, [45,46,47,48,49,50,51,52,53]),
        (6, [54,55,56,57,58,59,60,61,62]),
        (7, [63,64,65,66,67,68,69,70,71]),
        (8, [72,73,74,75,76,77,78,79,80])
    ]

    for row_number, squares in cases:
        assert sudoku.get_squares_by_row(row_number) == squares


def test_get_variable_names_by_square_returns_729_unique_values():
    variable_names = set([])

    for row in range(0,9):
        for square in sudoku.get_squares_by_row(row):
            for variable_name in sudoku.get_variable_names_by_square(square):
                variable_names.add(variable_name)
    
    assert len(variable_names) == 81 * 9 ##9 Unique values per square