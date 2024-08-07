# Passing normal arguments.
# Here order matters
def my_fun(a, b, c):
    print(f"A = {a}, B = {b}, C = {c}")

my_fun(20,10,30)

# Passing arguments with keyword: Keyword argument.
# Here order doesn't matter.
def my_function(a, b, c):
    print(f"A = {a}, B = {b}, C = {c}")

my_function(b = 20, c = 30, a = 10)