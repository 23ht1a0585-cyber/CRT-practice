
# name = input("Enter Employee Name: ")
# salary = input("Enter Employee Salary: ")
# with open("employee.txt", "a") as file:
#     file.write(name + "," + salary + "\n")

# print("\n--- Employee Data Saved ---")


# total_expenditure = 0

# print("\n--- EMPLOYEE REPORT ---")
# with open("employee.txt", "r") as file:
#     for line in file:
        
#         parts = line.strip().split(",")
        
#         emp_name = parts[0]
#         emp_salary = float(parts[1]) 
        
        
#         print("Name: " + emp_name + " | Salary: " + str(emp_salary))
        
        
#         total_expenditure = total_expenditure + emp_salary

# print("-----------------------")
# print("Total Salary Expenditure: " + str(total_expenditure))


# class Employee:

#     def write_file(self):
#         try:
#             f = open("emp.txt", "w")

#             n = int(input("Enter number of employees: "))
#             self.total = 0

#             for i in range(n):
#                 emp_id = input("Enter ID: ")
#                 name = input("Enter Name: ")
#                 salary = float(input("Enter Salary: "))

#                 self.total += salary

#                 f.write(emp_id + "," + name + "," + str(salary) + "\n")

#             f.close()
#             print("Total Salary:", self.total)

#         except ValueError:
#             print("Invalid input!")

#     def read_file(self):
#         try:
#             f = open("emp.txt", "r")

#             print("\nEmployee Report:")
#             for line in f:
#                 data = line.split(",")
#                 print("ID:", data[0], "Name:", data[1], "Salary:", data[2])

#             f.close()

#         except FileNotFoundError:
#             print("File not found!")


# # object creation
# obj = Employee()

# # function calls
# obj.write_file()
# obj.read_file()



# '''word frequency analyzer
# company wants to analyze the text
# 1. read contents from data.txt
# 2.count the frequency of each word
# 3.display most repeated word
# 4.handle the exceptions'''

# class WordFrequency:
#     def __init__(self):
#         self.freq = {}

#     def analyze(self):
#         try:
#             with open("data.txt", "r") as file:
#                 words = file.read().lower().split()

#             for word in words:
#                 self.freq[word] = self.freq.get(word, 0) + 1

#             print("Word Frequencies:")
#             for word, count in self.freq.items():
#                 print(word, ":", count)

#             max_word = max(self.freq, key=self.freq.get)
#             print("\nMost Repeated Word:", max_word)
#             print("Frequency:", self.freq[max_word])

#         except FileNotFoundError:
#             print("Error: data.txt not found")

#         except Exception as e:
#             print("Error:", e)


# obj = WordFrequency()
# obj.analyze()

# n = int(input("Enter a number: "))

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# import random
# print(random.randint(1, 100)

# import math

# r = float(input("Enter radius of circle: "))
# area = math.pi * r * r

# print("Area of circle is:", area)
# import random

# print(random.randint(1, 6))

# import datetime

# birth_year = 2005
# current_year = 2026

# print("Age:", current_year - birth_year)