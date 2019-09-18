#Times table

verified = False

while True:
        print("Welcome to the times table calculator.") ### SRC - no need to indent twice
    while not verified: 
        table = -1
        while table < 1 or table > 20:
            table = int(input("What table [1-20]?"))
        #end while
        table2 = -1
        while table2 < 1 or table2 > 20:
            table2 = int(input("Please confirm which table you would like to select?"))
        #end while
        if table == table2:
            print("You have selected the", table2, "times table.")
            verified = True
        else:
            print("Your selected tables do not match, please try again.")
        #end if
    #end while
            
    verified = False
    
    while not verified:
        rows = -1
        while rows < 1 or rows > 20:
            rows = int(input("How many rows [1-20]?"))
        #end while
        rows2 = -1
        while rows2 < 1 or rows2 > 20:
            rows2 = int(input("Please confirm how many rows you would like to select?"))
        #end while
        if rows == rows2:
            print("You have selected", rows2, "rows.")
            verified = True
        else:
            print("The number of selected rows do not match, please try again.")
        #end if
    #end while
            
    for item in range(1, rows2+1):
        print (item * table2)
    #next

    print("Do you want to use it again? (Y/N)") 
    ans = input()
    if ans == 'n' or ans == 'N':
        print("See you again soon!")
        break
    #end if
#end while
