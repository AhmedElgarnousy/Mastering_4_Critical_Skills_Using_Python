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
#class EmployeesManagerClass:
#class FrontEndClass:

class Employee:
  def __init__(self,name ,salary, address ):
    self.name = name  
    self.salary = salary  
    self.address = address 

#Enter employee data

print("""Program Choices:
 1-Add new employee
 2- Print all employees
 3-Delete by age
 4-Update Salary by name
 5-End the program
                         """)
ret = list(map(int , input('enter number from 1 - 5: ')))
      #handle string input to go to else block

      #
if ret == 1:
  print('enter employee data: ')
  name = input('Enter the name: ')
  name = Employee()
  age = int(input('Enter the age: '))
  salary = float(input('Enter the salary: '))

elif ret == 2:
  print('**employees list **')
elif ret == 3:
  print('Delete by age')
elif ret == 4:
  print('Update Salary by name')
elif ret == 5:
  print('End the program')
else:
  print('Invalid input, Try again!') 

