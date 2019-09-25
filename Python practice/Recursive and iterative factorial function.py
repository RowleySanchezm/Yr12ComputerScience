#Recursive factorial function

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
    #end if
#end function


num = int(input("Enter a number: "))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",recur_factorial(num))
#end if




#Iterative factorial function

def iterative_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    #end for
    return result
#end function


num1 = int(input("Enter a number: "))

if num1 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num1 == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num1,"is",iterative_factorial(num1))
#end if
