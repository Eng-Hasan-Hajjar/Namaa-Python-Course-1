"""
maan 80
Abd fattah  90
ismail 57
manaf 65
gith 57
sedra 61
jaber 21
obia 16
Bhaa 24
lama 3
hussam 2
ahmad  1

"""

import platform as plat
x=plat.system()
print(x)

y=dir(plat)
print(y)

import module1 as m
print(m.myfuncmodule()) 
print(m.ccc) 
y=dir(m)
print(y)
print(m.dictionary["name"])

from module1 import dictionary
print(dictionary["name"])

## math--module 
##min() max()
import math
y=dir(math)
print(y)
x=min(5,10,12)
y=max(5,10,12)
print((5,10,12),"min",x,"max" ,y)

##abs()
x=abs(-5.2)
print("abs", x)

## pow(4,2)

x= pow(4,2)
print(x)

## factorial

x= math.factorial(3)
print(x)
x= math.sqrt(16)
print(x)



x= math.ceil(3.2)
print(x)
x= math.floor(3.9)
print(x)

x=math.pi
print(x)


x=math.e
print(x)



##abd fattah
def myfunc():
    n=4
    return n**2
myfunc()
print(myfunc())

##manaf


##bahaaa
x=3
y=4
d=x**y
print(d)



def power( base , exp):
    x = base ** exp
    return x

y=power(4,3)    
print(y)
print(power(4,3))

## try except else finally


try:
    print(ppp)
except:
    print("there is exception 105")    

"""
##homwork multy except
try:
    print(ppp)
except:
    print("there is exception 105")    
except:
    print("there is exception 105")    
"""
try:
    print("ppp")
except:
    print("there is exception 105")    
else:
     print("there is else ")   
finally:
     print("there is finally ") 




## files
try:
    f=open("text2.txt")
except:
    print("there is exception file ")    



