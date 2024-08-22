import random

MAX_LINES = 3
MAX_BET = 5000
MIN_BET = 500

ROWS = 3
COLS = 3

symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        column.append(column)

    return columns

def deposit():                                                         
    while True:                                                         
        amount = input ("How much would you like to deposit? PHP ")        
        if amount.isdigit():                                            
            amount = int(amount)                                        
            if amount > 0:                                              
                break                                                   
            else:                                                       
                print ("Amount must be greater than 0.")
        else:                                                           
            print("Please enter a number")    

    return amount                                                      


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")     
        if lines.isdigit():                                                                                    
            lines = int(lines)                                           
            if 1 <= lines <= MAX_LINES:                                      
                break   
            else:
                print ("Enter a valid number of lines.")                     
        else:
            print("Please enter a number.")                                  

    return lines                                                             

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? PHP ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:        
                break
            else:
                print(f"Amount must be between PHP{MIN_BET} - PHP{MAX_BET}.")   
            print("Please enter a number.")

    return amount

    
def main(): 
    balance = deposit()                               
    lines = get_number_of_lines()                       
    while True:                                         
        bet = get_bet()
        total_bet = bet * lines                         
        if total_bet > balance:                                                                            
            print (f"You do not have enough to bet that amount, your current balance is: PHP{balance}")
        else:
            break

    print(f"You are betting PHP{bet} on {lines} lines. Total bet is equal to: PHP{total_bet}")          
    
main()          
    
