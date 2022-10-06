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
# Employee class: Just holds the data and basic function for it

class Employee:
    def __init__(self,name ,age ,salary ):
      self.name = name  
      self.salary = salary  
      self.address = age 
    def __str__(self) :
      return 'Employee: ' + self.name +' has age ' + str(self.age)+ ' and salary '+ str(self.salary)

   

#class EmployeesManagerClass: Holds a list of employees and has implementation for the menu options
class EmployeesManager:
    def __init__(self):
        self.Employees_List = []

    def Add_New_Emp(self):
        Employee.name = input('Enter the name: ')
        Employee.age = int(input('Enter the age: '))
        Employee.salary = float(input('Enter the salary: '))
        object = Employee(Employee.name , Employee.age , Employee.salary)
        self.Employees_List.append(object)

    def List_Emps(self):
        print('**employees list **')
        if len(self.Employees_List) == 0:
            print('No employees at the moment!')
        for emp in self.Employees_List:
            print(emp)

    def find_emp_by_name(self):
        print('Delete by age')

    def Update_Salary_by_name(self):
        print('Update Salary by name')

    def Del_emps_with_age_Range(self):
        print('End the program')


#class FrontEndClass:   Print the menu, get a choice and call the employees manager
class FrontEndClass:
    def __init__(self):
        self.Emp_Mng = EmployeesManager()

    ret = int(input('enter number from 1 - 5: '))

    if ret == 1:
        print('enter employee data: ')
        Self.Emp_Mng.Add_New_Emp()


    # Print the menu
    print("""Program Options:
     1-Add new employee
     2-Print all employees
     3-Delete by age
     4-Update Salary by name
     5-End the program
                               """)






