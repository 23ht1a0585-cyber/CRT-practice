#problem1:
#Create parent class Animal with method sound()

# Parent class
class Animal:
    def sound(self):
        print("Animal makes sound")

# Child class
class Dog(Animal):
    pass

# Create object of Dog
dog = Dog()

# Call inherited method
dog.sound()