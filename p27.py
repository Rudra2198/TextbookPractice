class Complex:
    def __init__(self,real,imag):
        self.r = real
        self.i = imag

    def f(self):
        print("Hello World!")


a = int(input("Enter number : "))
b = int(input("Enter second number : "))
        
x = Complex(a,b)
print(x.r + x.i)

fun = x.f #<---- Method Object

x.counter = 1 # <---- Instance Object

while x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)
print(fun()) #<---- calling the method object later
del x.counter #<---- deleting the Instance Object

