"""
maan 80
Abd fattah  87
ismail 56
manaf 64
gith 57
sedra 58
jaber 21
obia 16
Bhaa 23
lama 3
hussam 2
ahmad  1

"""
"""

class Animal:
    def _init_(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic sound")

    def info(self):
        print(f"Name: {self.name}, Species: {self.species}")

class Dog(Animal):
    def _init_(self, name, breed, age, color):
        # استدعاء البناء من الفئة الأساسية
        super()._init_(name, "Dog")
        self.breed = breed
        self.age = age
        self.color = color

    # إعادة تعريف الدالة make_sound
    def make_sound(self):
        print("Woof! Woof!")

    # إضافة دالة جديدة خاصة بالفئة Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball!")

    # إضافة دالة جديدة لعرض العمر
    def display_age(self):
        print(f"{self.name} is {self.age} years old.")

    # إضافة دالة جديدة لعرض اللون
    def display_color(self):
        print(f"{self.name} is {self.color}.")

    # إعادة تعريف دالة info لإضافة سلالة وعمر ولون الكلب
    def info(self):
        super().info()
        print(f"Breed: {self.breed}, Age: {self.age}, Color: {self.color}")

# إنشاء كائن من الفئة الأساسية Animal
generic_animal = Animal("Generic Animal", "Unknown")
generic_animal.info()      # الناتج: Name: Generic Animal, Species: Unknown
generic_animal.make_sound() # الناتج: Some generic sound

# إنشاء كائن من الفئة الفرعية Dog
my_dog = Dog("Buddy", "Golden Retriever", 5, "Golden")
my_dog.info()              # الناتج: Name: Buddy, Species: Dog, Breed: Golden Retriever, Age: 5, Color: Golden
my_dog.make_sound()        # الناتج: Woof! Woof!
my_dog.fetch()             # الناتج: Buddy is fetching the ball!
my_dog.display_age()       # الناتج: Buddy is 5 years old.
my_dog.display_color()     # الناتج: Buddy is Golden.

"""
## kivy

## Android sdk java
## apk 
## beeware.com  apk from python 

## تعدد الأشكال

##len()
x="welcome to our course"
print("ex1 for len in string: with Bahaa: ",len(x))


## len() with tuple
y=(10,20,30)
print("ex2 for len in tuple: with Sedra: ",len(y))


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive!")
class Boat:
    def __init__(self,brand,model):
      self.brand=brand
      self.model=model
    def move(self):
        print("Sailing!")


class Plane:
    def __init__(self,brand,model):
      self.brand=brand
      self.model=model
    def move(self):
        print("fly!")

car1=Car("bmw","2024")
boat1=Boat("yamah","2016")
plane1=Plane("nnn","2301")

for x in (car1,boat1,plane1):
    x.move()


class Vehicle2:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Move!")

class Car(Vehicle2):
    pass


class Boat(Vehicle2):
    
    def move(self):
        print("Sailing!")


class Plane(Vehicle2):
    
    def move(self):
        print("fly!")


car1=Car("bmw","2024")
boat1=Boat("yamah","2016")
plane1=Plane("nnn","2301")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()

## scope

def myfunc():
    x10=300
    def myinnerfunc():
           print(x10)
    myinnerfunc()
myfunc()   



x11=11
def myfunc11():
    print(x11)
  
myfunc11()   
print(x11)


x12=12
def myfunc12():
    x12=13
    print(x12)
  
myfunc12()   
print(x12)






x13=13
def myfunc13():
    global x13
    x13=14
    print(x13)
  
myfunc13()   
print(x13)





def myfunc():
    x15=300
    def myinnerfunc():
        nonlocal x15
        x15=250
    myinnerfunc()
    return x15
print(myfunc())  


## modules
import module1
print(module1.myfuncmodule()) 
print(module1.ccc) 

import module1 as m
print(m.myfuncmodule()) 
print(m.ccc) 


