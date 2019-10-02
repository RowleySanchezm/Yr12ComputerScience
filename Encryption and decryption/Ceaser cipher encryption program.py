#Caesar Cipher encryption program

def encrypt(text,s): 
    result = "" 
    for i in range(len(text)): 
        char = text[i]
    #Next i
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65)
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97)
        #End if
    return result
#End function

shift = 0
selection = 0
while selection != 3:
    selection = int(input("Please enter 1 if you would like to use imported text file, 2 if you would like to enter your own text or 3 to leave program: "))
    if selection != 3:
        shift = int(input("Enter shift: "))
    if selection == 1:                  
        text = open("test.txt", "rt")
        data = text.read()
        text.close()
        print(data)

        text = open("test.txt","rt")
        for a in text:
            print(encrypt(a,shift))
        #next a
        text.close()
    elif selection == 2:
        plain_text = input("Please enter the plain text that you would like to encrypt: ")
        print(encrypt(plain_text,shift))
    elif selection == 3:
        print("You have selected to leave the program.")
    else:
        print("Sorry but the number you have entered is not valid.")
    #end if
#end while
print("Have a good day.")
