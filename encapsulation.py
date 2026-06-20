#what is encapsulation?
#binding data and methods together into a single unit

#And:
#restricting direct access to data

#encapsulation protects the data from 
#1. unauthorized acesss
#2.accidential modifications

#Similarly In opps:
#Data is hidden inside the class accesses using methods

#key-idea:
# data+ methods
#it comnbined into a single unit 
#controlled access


#Features of Encapsulation :
#1.security
#2. data hiding 
#3. controlled access
#4.better maintananceass Bank:
#    def__init__(self):
#    self.balance = 10000

#    def deposit(self,amount):
#      self.balance +=amount
# def show_balance(self):
#   print(self.balance)


# data hiding 

#goal:prevent the data modifications misuse of data 
# public  : bydefault
# protected : single_underscore
# private  : __double__underscore

# 1. public: memberes can be acccessible everywhere
#default acess type in python
# class Student:
#     def __init__(self):
#         self.__name = ""   # private variable

#     def set_name(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name


# s = Student()

# s.set_name("Ravi")
# print(s.get_name())

# class Student:
#     _name = "Ravi"   # protected

# s = Student()
# print(s._name)

#s= student()
#print(s._name)

#it says dont access it directly
# WHERE TO USE :
# 1. during inheritance
# 2. for internal usage



#PRIVATE : IN IHIS WE UNS  DOUBLE UNDERSCORE

#used for STRONG DATA HIDING 

# class Student:
#     __marks = 95

# s = Student()

# print(s._Student__marks)


#PRIVATE:
# IT IS NOT FULLY PROTECTED ..IT JUST PROTECTED FROM ACCIDENTS 

# class Student:
#     def __init__(self):
#         self.__marks = 90   

# s = Student()

# print(s._Student__marks)


# class BankAccount:
#     def __init__(self):
#         self.__balance = 5000

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         self.__balance -= amount


# acc = BankAccount()

# acc.deposit(1000)
# acc.withdraw(500)

# print(acc._BankAccount__balance)


#GETTER AND SETTER:
#getter means it can only the data but setter it can update 


#task:

# class BankAccount:
#     def __init__(self):
#         self.__balance = 1000

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount

# b1 = BankAccount()

# print(b1.get_balance())

# b1.set_balance(2000)

# print(b1.get_balance())





#class student
   