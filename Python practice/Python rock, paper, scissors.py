#Rock, paper, scissor game

while True: ### SRC - Please use more meaningful conditions
    print("Please select: 1. Rock 2. paper 3. scissor ")
    choice = int(input("Your turn: "))
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: "))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
    print("You selected, ", choice_name)
        
    import random  ### SRC - imports should be at the top of the file
    for x in range(1):
        comp_choice = random.randint(1, 3)
        if comp_choice == 1: 
            comp_choice_name = 'Rock'
        elif comp_choice == 2: 
            comp_choice_name = 'paper'
        else: 
            comp_choice_name = 'scissor'
        print("The computer selected, ", comp_choice_name)
### SRC - Really good if statement
    if((choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice ==1 )): 
        print("paper wins => ", end = "") 
        result = "paper"
              
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("Rock wins =>", end = "") 
        result = "Rock"
    else: 
        print("scissor wins =>", end = "") 
        result = "scissor"

    if result == choice_name: 
        print("<== User wins ==>") 
    else: 
        print("<== Computer wins ==>") 

    print("Do you want to play again? (Y/N)") 
    ans = input()
    if ans == 'n' or ans == 'N': 
        break  ### SRC - please do not use break! 
