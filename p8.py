inp = int(input("Enter a number : "))
fact = 1

if inp == 0:
    print("Try again!")
elif inp < 0:
    print("Try again!")
else:
    while (inp > 0):
        fact = fact * inp
        inp -= 1
print("The factorial is ", fact)