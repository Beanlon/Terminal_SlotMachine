#The comments are indicating the meaning behind the code with line by line expanation.


#These are unchanging values which means these are variables that are not randomized
MAX_LINES = 3
MAX_BET = 5000
MIN_BET = 500

#These lines uses deposit function, inputing a specific amount with loop statments.

def deposit():                                                          #Line 11 - def is used to specify a function this time using deposit
    while True:                                                         #Line 12 - While true starts an infinite loop that will keep running until a break statement is encountered.
        amount = input ("How much would you like  to deposit? PHP ")        #Line 13 - Amount being the variable is comprised of an input which is stored as a string prompting the user to input an amount
        if amount.isdigit():                                            #Line 14 - Checks if the said variable which is amount is a digit which is a poitive integer (eg. 1-100, etc.)
            amount = int(amount)                                        #Line 15 - Turns numeric string 'amount' into an integer
            if amount > 0:                                              #Line 16 - Checks if the converted integer is greater than 0. If true, it proceeds to the next step.
                break                                                   #Line 17 - Break allows for the exit of the loop, indicating that a valid deposit amount has been entered
            else:                                                       #Line 18-19 - It is an else statement where if it does not comply with the condition ("If the number is less than or equal to  0")then it shows a print statement
                print ("Amount must be greater than 0.")
        else:                                                           #Line 20-21 - It is another else statement, has similar properties but with a different condition cnnected to it ("If the input was a non-numeric value") 
            print("Please enter a number")    

    return amount                                                       #Line 23 - returns amount once the loop is exited


#Since these sets of lines are reapeting with similar lines of code from the previous function I will only explain the changes

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")     #Line 30 - f-string is a string that dynamically inserts of "MAX_LINES" into the string
        if lines.isdigit():                                                                                    
            lines = int(lines)                                           
            if 1 <= lines <= MAX_LINES:                                      #Line 33 - it shows a conditional where if  the "lines variable is greater than or equal to 1  but less than or equal to 3 then it wil proceed to the next line"
                break   
            else:
                print ("Enter a valid number of lines.")                     #Line 36 - If the conditions from line 33 are not meant then it will print out this statment asking for a proper input
        else:
            print("Please enter a number.")                                  #Line 38 - If the conditions from line 31 is not meant then it will print out this statement asking for a numerical value

    return lines                                                             #Line 40 - returns the number of line once the loop is finished

#Since these sets of lines are reapeting with similar code I will only explain the changes

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? PHP ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:        #Line 49 - The conditions asked are somewhat similar to line 33 however this time it uses the  variable "amount" and the constant variables {MIN_BET} and {MAX_BET}
                break
            else:
                print(f"Amount must be between PHP{MIN_BET} - PHP{MAX_BET}.")   #Line 50 - If the input doesn't meet the required condition, the code prints a message using an f-string. The message indicates that the amount must be between {MIN_BET} and {MAX_BET} (e.g., 500 and 5000, as defined in lines 6-8).
            print("Please enter a number.")

    return amount

#This new lines of code are the whole systme behind the betting system, the previous lines of code were only only for inputing values for said variables
    
def main(): 
    balance = deposit()                                 #Line 62 - The deposit function is now recognized as balance 
    lines = get_number_of_lines()                       
    while True:                                         #Line 64 - A while true loop will be used in order to begin the betting system 
        bet = get_bet()
        total_bet = bet * lines                         #Line 66 - total_bet is a variable that multiplies your bet per line by the number of lines chosen, calculating your total wager.
        if total_bet > balance:                                                                            #Line 67 - 73 - an if-else function is used where if your total_bet exceeds your balance it will print an f-string statement, if it complies it breaks
            print (f"You do not have enough to bet that amount, your current balance is: PHP{balance}")
        else:
            break

    print(f"You are getting PHP{bet} on {lines} lines. Total bet is equal to: PHP{total_bet}")          #Line 70 - a statement will show after breaking from the if-else loop with another f-function
    
main()          #Line 72 - main() will be the starting point throughout the whole code, without this nothing will run despite having the code
    
