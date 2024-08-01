# String data type : Immutable data type
name = 'Hriody'
Name = "Hridoy"

# Triple quote accept multiple line string.
Nam = '''Hridoy
         Hasan'''
print(len(Nam))
print("Hridoy"[2])

# Print string using for loop:
for el in Nam:
    print(el, end=" ")
print()

# Indexing in python:
"""
Index:     0  1  2  3  4  5
           P  y  t  h  o  n

Negative Index: -6 -5 -4 -3 -2 -1
                 P  y  t  h  o  n
"""

# String slicing : string[start,end,step]

NamE = "Hridoy Hasan"
# Output : Hridoy Hasan
print(NamE[:])

# Output : Hridoy Hasan
print(NamE[:len(NamE)])

# Output : Hridoy Hasan
print(NamE[0:])

# Output : Hridoy Hasan
print(NamE[0:len(NamE)])

# Output : doy Ha
print(NamE[3:9])

# Output : Hio aa
print(NamE[::2])

# Output :Hriody Hasa
print(NamE[-12:-1])

# Reverse sting
print(NamE[::-1])

