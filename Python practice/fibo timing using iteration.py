def fibrec(n):
    fibNumbers = [0,1] #list of first two Fibonacci numbers
    for i in range(2,n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    #next i
        return fibNumbers[n]
#end function

import time

nterms = int(input("How many terms? "))

startTime1 = time.clock()

if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(fibrec(i))
    #Next
#End if

endTime1 = time.clock()

print(startTime1, endTime1)
