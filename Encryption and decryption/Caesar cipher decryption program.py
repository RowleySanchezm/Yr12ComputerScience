#Caesar Cipher decryption program
### SRC - This is neat and simple, but I did get "n" for space.
def decrypt(cipher_text,s): 
    result = "" 
    for i in range(len(cipher_text)): 
        char = cipher_text[i]
    #Next i
        if (char.isupper()): 
            result += chr((ord(char) - s-65) % 26 + 65)
        else: 
            result += chr((ord(char) - s - 97) % 26 + 97)
        #End if
    return result
#End function

Cipher_text = input("Please enter the cipher text: ")
shift = int(input("Enter shift: "))

print(decrypt(Cipher_text,shift))
