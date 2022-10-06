"""
ProjectName:Employees System
Author: Ahmed Kamal
Description:
● Help our factory in managing the employees. 
● Create a program that provides the following operations:
○ Enter your choice:
○ 1) Add new employee
○ 2) Print all employees
○ 3) Delete by age
○ 4) Update Salary by name
○ 5) End the program
● You will keep the program running forever. 
○ Display the choices and user input from 1 to 5

"""

# Employee class
#  Just holds the data and basic function for it
class Employee:
  def __init__(self,name ,age ,salary ):
    self.name = name  
    self.salary = salary  
    self.address = age 

  def __str__(self) :
    return 'Employee: ' + self.name +' has age ' + str(self.age)+ ' and salary '+ str(self.salary)
 
#class EmployeesManagerClass:
#   Holds a list of employees and has implementation for the menu options
#class EmployeesManagerClass:
#  Employees_List = []


#class FrontEndClass:
#  Print the menu, get a choice and call the employees manager
#class FrontEndClass:

print("""Program Options:
 1-Add new employee
 2-Print all employees
 3-Delete by age
 4-Update Salary by name
 5-End the program
                           """)

ret = int(input('enter number from 1 - 5: '))
Employees_List = []
if ret == 1:
  
  print('enter employee data: ')
  Employee.name = input('Enter the name: ')
  Employee.age = int(input('Enter the age: '))
  Employee.salary = float(input('Enter the salary: '))
  Employees_List.append(Employee.name )

elif ret == 2:
  print('**employees list **')
  print(Employees_List)

elif ret == 3:
  print('Delete by age')
elif ret == 4:
  print('Update Salary by name')
elif ret == 5:
  print('End the program')
else:
  print('Invalid range, Try again!') 
