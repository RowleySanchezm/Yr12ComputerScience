#Caesar Cipher program

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


text = open("test.txt", "rt")
data = text.read()
text.close()
print(data)

shift = int(input("Enter shift: "))

text = open("test.txt","rt")
for a in text:
    print(encrypt(a,shift))
text.close()

