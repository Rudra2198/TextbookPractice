try:
    a=15
    b=0
    print(a/b)
except TypeError:
    print("Wrong datatype to perform division")
except ZeroDivisionError:
    print("Division by zero not allowed")

print("Out of try except blocks")
