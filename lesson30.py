"""
maan 80
Abd fattah  80
ismail 56
manaf 54
gith 52
sedra 54
jaber 21
obia 16
Bhaa 17
lama 3
hussam 2
ahmad  1

"""

from pubgclasses.player import Player
from pubgclasses.map import Map
from pubgclasses.vehicle import Vehicle
from pubgclasses.weapon import Weapon


## creat player
## ex1
player1=Player("player1")
player2=Player("player2")
player3=Player("player3")

player1.move(10,20)
player1.take_damage(20)
player1.pick_up_weapon("AKM")


player2.move(1,20)
player2.take_damage(0)
player2.pick_up_weapon("M4")

## create weapons
akm=Weapon("akm",30)
m4=Weapon("M416",25)

print(akm)
print(player1)


##create vehilce
jeep=Vehicle("jeep",30)
buggy=Vehicle("buggy",20)


jeep.drive("school")
buggy.drive("fram")

erangle=Map("Erangle","8*8km")
erangle.add_player(player1)
erangle.add_player(player2)
erangle.add_player(player3)


### الوراثة

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)

per=Person("manaf","hamad")
per.printname()        

class Student(Person):
    pass 

stud=Student("abd","hamad")
stud.printname()

class Student(Person):
    def __init__(self,fname,lname,mark):
        self.fname=fname
        self.lname=lname
        self.mark=mark
    def printname(self):
        print(self.fname,self.lname,self.mark)

stud=Student("abd2","hamad",20)
stud.printname()







class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
  
class Student(Person):
    def __init__(self,fname,lname,grad):
      super().__init__(fname,lname)
      #Person.__init__(fname,lname)
      self.gradyear=grad
        
    def cul(self):
        print("print hello")   
stud=Student("abd3","hamad",2019)
stud.printname()
print(stud.gradyear)
stud.cul()


## ex1  for inheritance
class Animal:
    def __init__(self,pname):
        self.name=pname
    def move(self):
        print(f"{self.name} is moving")
    #abstuct method
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")    

class Dog(Animal):
    def __init__(self,pname,pbreed):
        super().__init__(pname)
        self.breed=pbreed        
    def fetch(self):
        print(f"{self.name} is fetching the ball")
    #abstruct method
    def speak(self):
         print(f"{self.name} says .....")

dog=Dog("losi","white")
dog.move()
dog.speak()
dog.fetch()

## ex2  for inheritance
class Animal:
    def __init__(self,pname):
        self.name=pname
    def move(self):
        print(f"{self.name} is moving")
    #abstuct method
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")    

class Mammal(Animal):
    def __init__(self,pname,color):
        super().__init__(pname)
        self.color=color
    def describe(self):
        print(f"{self.name} color is  {self.color}")
  



class Dog(Mammal):
    def __init__(self,pname,color,pbreed):
        super().__init__(pname,color)
        self.breed=pbreed        
    def fetch(self):
        print(f"{self.name} is fetching the ball")
    #abstuct method
    def speak(self):
         print(f"{self.name} says .....")

dog=Dog("losi","white","breed")
dog.move()
dog.describe()
dog.speak()
dog.fetch()



