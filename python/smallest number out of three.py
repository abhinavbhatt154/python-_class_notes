def minimum(a, b, c): 
   list = [a, b, c] 
   return min(list) 
# Driven code  
x = int(input("Enter First number:"))
y = int(input("Enter Second number:"))
z = int(input("Enter Third number:"))
print("Smallest Number is :",minimum(x, y, z))