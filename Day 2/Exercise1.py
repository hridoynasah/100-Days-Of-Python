# Solution 1 :
Num = int(input("Type two digit number: "))
a = Num % 10
Num = Num // 10
b = Num % 10
print(a+b)

# Solution 2:
Num = input("Type two digit number: ")
a = int(Num[0])
b = int(Num[1])
print(a + b)


