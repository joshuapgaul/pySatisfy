
from structures import Variable, Literal, NEGATIVE_LITERAL, POSITIVE_LITERAL, Clause, Circuit, SATStatus

##3 X 3 X 3 Sudoku (standard)

##There are 9 variables per square, denoting the 9 different options for filling that square

## Here's the grid
#Col0 -> Col8
##|--------|---------|---------|
##|0, 1, 2 | 3, 4, 5 | 6, 7, 8 | Row 0
##|9,10,11 | 12,13,14| 15,16,17|       -> Boxes 0, 1, 2
##|18,19,20| 21,22,23| 24,25,26|
##|--------|---------|---------|
##|27,28,29| 30,31,32| 33,34,35|
##|36,37,38| 39,40,41| 42,43,44|       -> Boxes 3, 4, 5
##|45,46,47| 48,49,50| 51,52,53|
##|--------|---------|---------|
##|54,55,56| 57,58,59| 60,61,62|
##|63,64,65| 66,67,68| 69,70,71|       -> Boxes 6, 7, 8
##|72,73,74| 75,76,77| 78,79,80| Row 8
##|--------|---------|---------|


##Each square needs 9 options, denoting the 9 different numbers that could fill that square
def get_variable_names_by_square(square_number):
    return range(square_number * 9, (square_number + 1) * 9)

def get_squares_by_column(column_number):
    return [column_number + (row * 9) for row in range(0, 9)]

def get_squares_by_row(row_number):
    return [(9 * row_number) + col for col in range(0,9)]
