
'''# example of Polymorphism
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    print('hi 6')
    def make_sound(self):
        return 'woof'
    
class Cat(Animal):
    def make_sound(self):
        return 'meow'
    
class Bird(Animal):
    def make_sound(self):
        return 'tweet'
    

def Animal_sound(animal):
    print('hi 19')
    print(animal.make_sound(animal))


dog=Dog

Animal_sound(dog)'''


'''class Shape:
    def CalculateArea(self):
        pass

class Circule(Shape):
    def __init__(self,radius):
        self.radius=radius

    def CalculateArea(self):
        return f'Area of Circule : {3.14 * self.radius * self.radius}'

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length= length
        self.width=width

    def CalculateArea(self):
        return f'Area of Rectangle : {self.length * self.width}'




circule =Circule(7)
rectangle = Rectangle(5,4)
  
shapes = [circule,rectangle]

for shape in shapes:
    print(shape.CalculateArea())'''


#method overloading

class math:
    def add(self,a,b,):
        return a+b
    def add(self,a,b,c=None):
        return a+b+c
a = math()
print(a.add(3,5,7)) 

'''class math:
    def add(self,a,b,c=None):
        if not c==None:
            return a+b+c
        else:
            return a+b
        
b = math()
print(b.add(8,8))
print(b.add(8,8,8))'''