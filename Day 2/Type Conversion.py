# Input function always takes input as string :
z = input()  # Input : 10
y = input()  # Input : 20
sum = y + z
# Output : 1020
print(sum)
# Output : <class 'str'> <class 'str'>
print(type(z), type(y))

# Here we need type conversion :
x = int(input("Enter the value of x : "))  # Input : 10
a = int(input("Enter the value of a : "))  # Input : 20

s = x + a
# Output : 30
print(s)
b = 20
c = float(b)
print(c)