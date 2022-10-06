class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  'Employee ' + self.name + ' is '+ str(self.age) + ' years old ' 

    def __repr__(self):
        return  'Employee (name="' + self.name + '", age='+ str(self.age) + ')'

Ahmed = Employee('Ahmed' , 21)

print(str(Ahmed))
print(repr(Ahmed))