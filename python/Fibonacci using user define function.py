#Writing python code to print Fibonacci series

def fibonacci(n):
    if(n == 0):
         return 0  
    elif (n == 1):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n = int(input ("how many term: "))
print ("Fibonacci series: ")
for n in range(0, n):
    print (fibonacci(n))
