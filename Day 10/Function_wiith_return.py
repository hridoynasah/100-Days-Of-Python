# Function with return
def format_name(f_name, l_name):
    """Take a first and last name and format it to
    return the title case version of the name."""
    full_name = f_name.capitalize() + " " + l_name.capitalize()
    return full_name

first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()

full_name = format_name(l_name=last_name, f_name=first_name)
print(full_name)
