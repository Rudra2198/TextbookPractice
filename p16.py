name = input(" Enter file name ")
fobj = open(name)
for x in fobj:
    print(x,end="")


""" alternate method

    print(fobj.read()) """
