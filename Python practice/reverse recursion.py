#String reverse using recursion

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
    #End if
#End function

string = "star"
print("Reverse is " + reverse(string))
