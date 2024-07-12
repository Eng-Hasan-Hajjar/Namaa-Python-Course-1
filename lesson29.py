




class Player:
    name="Guest"
    idd="guest"
    def __init__(self,namee,iddd):
        self.name=namee
        self.idd=iddd

player1=Player("maan","manaf") 
print(player1.name)     
print(player1.idd)     


## __str__()
class Person:
 
    def __init__(self,namee,ageparam):
        self.name=namee
        self.age=ageparam
    def __str__(self):
        return f"{self.name}({self.age})"

pers=Person("bahaa",23) 
print(pers)     
 

#ex
class Person:
 
    def __init__(self,namee,ageparam):
        self.name=namee
        self.age=ageparam
    def __str__(self):
        return f"{self.name}({self.age})"
    def my_func_in_class(self):
        print("bahaa")
pers=Person("bahaa",23) 
print(pers)     
pers.my_func_in_class()
 

#ex
class Person:
 
    def __init__(self,namee,ageparam):
        self.name=namee
        self.age=ageparam
    def __str__(self):
        return f"{self.name}({self.age})"
    def my_func_in_class(abss):
        print("bahaa",abss.age)
pers=Person("bahaa",23) 
print(pers)     
pers.my_func_in_class()
pers.age=34
print(pers)

del pers.age
## print(pers) ## error
del pers



## example for my friends 



