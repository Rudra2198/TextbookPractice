

""" This is Single Inheritance """


class Animal:
    
    def Eat():
        print("This animal eats")


class Bird(Animal):

    Animal.Eat()
    print("This is a bird")

