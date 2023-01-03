num = 0

for num in range(10):
    if num == 4:
        break

    print("Number is",num)

print("Exit from loop\n")

for value in "welcome":
    if value == "o":
        continue
    print(value)

print("End of for loop\n")

num = 0

for num in range(10):
    if num == 5:
        pass

    print("Number is",num)
