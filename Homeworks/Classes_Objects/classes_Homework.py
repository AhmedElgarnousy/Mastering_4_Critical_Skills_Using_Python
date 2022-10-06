#Rectangle and Circle (Done)

"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area
      #  print('Rectangle Area is',self.area)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    pi =3.14
    def get_area(self):
        self.area = self.pi * (self.radius ** 2)
        return self.area


r = Rectangle(10 , 5) 

print(r.get_area())

Cir = Circle(5)
print(Cir.get_area())

"""

#Editor 
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area
      #  print('Rectangle Area is',self.area)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    pi =3.14
    def get_area(self):
        self.area = self.pi * (self.radius ** 2)
        return self.area

class Editor:
    def __init__(self):
        self.Rec = Rectangle(width , height)
    def create_rectangle(self, width, height):
        self.width = R
    def create_circle(self, radius):
    def change(self, factor):
    def print(self):


editor = Editor()
editor.create_rectangle(3 , 5)
editor.print()
#Rectangle area 15
editor.create_circle(5)
editor.change(2)
editor.print()
#Rectangle area 35
#Circle area 153.86

"""

#Homework 1: Our MyRange Class (Done)
"""
class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def has_next(self):
        if self.start < self.end:
            return True

    def get_next(self):
        item = self.has_next()
        if item == True:
            nextItem = self.start 
            self.start += self.step
            return nextItem

rng = MyRange(5, 10, 1)

while rng.has_next():
    print(rng.get_next(), end=' ') # 5 6 7 8 9
print()

rng = MyRange(5, 10, 2)
while rng.has_next():
    print(rng.get_next(), end=' ') # 5 7 9

"""


#Homework 2: Our MyRange Class (Flexible) (Done )

class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.idx = -1

    def has_next(self):
        if self.step < 0:
            if self.start > self.end:
            # step is negative
                return True

        # step is positive
        if self.start < self.end:
            return True
    def get_next(self):
        item = self.has_next()
        if item == True:
            if self.step < 0:     
                # step is negative
                nextItem = self.start 
                self.start += self.step
                self.idx +=1
                return self.idx , nextItem
            
            if self.step > 0:     
                # step is positive
                nextItem = self.start 
                self.start -= self.step
                idx +=1
                return idx , nextItem 

rng = MyRange(10, 5, -1)

while rng.has_next():
    print(rng.get_next(), end=' ') # 5 6 7 8 9
print()


