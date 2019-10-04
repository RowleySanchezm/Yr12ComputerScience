def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
    #End if
#End function
import time

nterms = int(input("How many terms? "))

startTime1 = time.clock()

if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))
    #Next
#End if

endTime1 = time.clock()

print(startTime1, endTime1)
