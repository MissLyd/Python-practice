import random

# constants
MAX_LINES = 3
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { # dictionary of symbols 
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = { # dictionary of values
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): # loop through every row that the user bet on
        symbol = columns[0][line]
        for column in columns: # loop through every column of the row
            symbol_to_check = column[line]
            if symbol != symbol_to_check: # if all symbols are the same, it's a win
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) # corrected index for lines

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .items gives you the key(symbol ex: A) and the item(count ex: 2)
        all_symbols.extend([symbol] * symbol_count) # simplifies appending multiple symbols

    columns = [] # initialize an empty list to store columns
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # copy of all_symbols list for each column
        # [:] is a slice operator to copy without affecting the other list
        
        for _ in range(rows):
            value = random.choice(current_symbols) # choose from current_symbols
            current_symbols.remove(value) # remove the chosen symbol to prevent repitition
            column.append(value)
        
        columns.append(column) # add the completed column to columns list

    return columns 


def print_slot_machine(columns):
    for row in range(len(columns[0])): # loop through every row
        for i,column in enumerate(columns): # loop through every column
            if i != len(column) - 1: # check if it's the last column
                print(column[row], end=" | ") # end= tells the code what to end each line with
            else:
                print(column[row], end="")
        print() # move to the next line after row is printed


def deposit():
    while True:
        balance = input("What would you like to deposit?: $")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number: $")
    return balance


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("The number of lines must be valid")
        else:
            print("Please enter a number: ")
        
    


def get_bet():
    while True:
        bet = input("What would you like to bet?: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet:
                return bet
        else:
            print("Please enter a number: $")
        
        

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet() 
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance} ")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines) # * passes every item of the list to the print statement
    
    return winnings - total_bet


def main():
    balance = deposit() 
    while True:
        print(f"Current balance is $ {balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

main()