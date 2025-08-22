# the computer asks user for input sudoku, and solves it
# the puzzle is a list of lists, each inner list representing a row in the puzzle
# each square of the puzzle is a (row,col) tupple
# empty spaces are represented by 0

# we ask the user to enter his puzzle
def get_puzzle():
    puzzle= []
    print("Enter each row one by one, seperate the numbers by spaces (use 0 for empty squares).")
    for r in range(9):
        while True: # Keeps asking until input is correct
            try:
                row = input(f"Row {r+1}: ").strip().split()
                if len(row) != 9:
                    print("Please enter 9 numbers seperated by spaces.")
                    continue # Loops back and tries again
                
                row = [int(num) for num in row] # Turning row into a list of integers, might raise a ValueError if input is not int

                puzzle.append(row) # Adding the row to the puzzle list
                break # Exiting the while loop for this row
            
            except ValueError:
                print("Only numbers between 0 and 9 accepted. Try again.") # In case input is not int
    
    return puzzle
            

def find_next_empty(puzzle):
    for r in range(9): # going through each row
        for c in range(9): # going through each column in each row
            if puzzle[r][c] == 0: # if it's an empty space
                return r,c
            
    return None,None # In the case of no empty spaces in the puzzle

def is_valid(puzzle,guess,row,col):
    # we're checkin if the guess the computer made is valid or not
    # starting with rows, transfering the row only

    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    
    # then columns, for each row represented by i, we're transfering the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # Now we're checking each 3 by 3 square
    # We have to figure out which square our guess is on first
    # So we're isolating the start of the row and start of the column of the square
    
    row_start = (row//3)*3 
    col_start = (col//3)*3

    # example: if i'm on row 6 and column 3, row_start = 6 and col_start = 3
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   |   |   |   |
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   |   |   |   |
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   |   |   |   |
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   | x | x | x |\
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   | x | x | x | > We're here
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   | x | x | x |/
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   |   |   |   |
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   |   |   |   |
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # |   |  `|   |   |   |   |   |   |   |
    #  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    for r in range(row_start, row_start +3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c] == guess:
                return False
    
    # if we passed all these tests then the guess is valid
    return True


def solve_sudoku(puzzle):
    # step 1: find an empty space to make a guess
    row, col = find_next_empty(puzzle)
    if row is None:
        return True # The puzzle is already complete
    
    # step 2: check if the guess is valid and place it
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            # step 3: reinitialize our puzzle with the guess, so it becomes an integrant part of it
            # that is done by recursively calling our function
            if solve_sudoku(puzzle):
                return True
            
        # step 4: if not valid or does not solve the puzzle, backtrack
        puzzle[row][col] = 0

    # step 5: if none of the combinations work, the puzzle is not solvable
    return False

# Optional: pretty printing the sudoku
def pretty_print_sudoku(puzzle):

    # First the horizental seperators between each three rows
    for r in range(9):
        if r%3 == 0 and r != 0:
            print("-"*21) # just counted how many i needed lol

        # Then the vertical separators between each three columns*
        # Since it's hard to seperate the row itself and insert inside it, we're gonna transfer it to a string and print it

        row = " " # Creating our string

        for c in range(9):
            if c%3 == 0 and c!= 0:
                row += " | " # Between every three numbers, a separator

            row += str(puzzle[r][c]) + " " # Adding the numbers in the row to the string with a space
        
        print(row)

example = get_puzzle()
print(solve_sudoku(example))
pretty_print_sudoku(example)
            