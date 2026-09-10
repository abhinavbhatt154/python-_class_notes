# Program to check if a number is prime or not

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable


def operation(x):
           if x>1:     
              for i in range(2, x):
                 if (x % i) == 0:
                     print(x, "is not a prime number")
                     break
              else: 
                 print(x, "is a prime number")
           else:             
             print(x, "is not a prime number")
operation(13)     
      
      