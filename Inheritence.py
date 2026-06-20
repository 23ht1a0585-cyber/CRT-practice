#Check the inheritance
class Animal:
    pass
class Dog(Animal):
    pass
c1 = Dog()
print(isinstance(c1,Animal))
print(issubclass(Dog,Animal))

class parent:
    def__init__(self):
       print("Construction called")
class child (parent):
    pass
c1 = child()   



                
















   


























         






















