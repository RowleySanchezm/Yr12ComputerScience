#Times table

table = -1
while table < 1 or table > 20:
    table = int(input("What table [1-20]?"))
    print("Please enter an integer between 1 and 20.")
#end while

rows = -1
while rows < 1 or rows > 20:
    rows = int(input("How many rows [1-20]?"))
    print("Please enter an integer between 1 and 20.")
#end while

for item in range(1, rows+1):
    print (item * table)
#next
