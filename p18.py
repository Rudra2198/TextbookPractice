try:
    print("Accepting 2 numbers from user")
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    z = x/y
except ValueError:
    print("ENTERED CHARACTER FOR DIVISION")
except ZeroDivisionError:
    print("Tried to divide by Zero")
else:
    print("else block")
    print("Division",z)
finally:
    print("finally block")
    x = 0
    y = 0
    print("Out of try,except,else and finally blocks")
