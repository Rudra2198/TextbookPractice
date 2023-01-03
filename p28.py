class Dog:
    kind = 'Canine'

    def __init__(self,name):
        self.name = name #<----- Instance Variable


d = Dog("Fido")
e = Dog("Buddy")

print(d.name)
print(d.kind)
print(e.name)
print(e.kind)
