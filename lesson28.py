"""
maan 80
Abd fattah  76
ismail 55
manaf 53
gith 48
sedra 52
jaber 21
obia 16
Bhaa 15
lama 3
hussam 2
ahmad  1

"""

## التعاودية وظيفة معن
#ex1
##4!=4*3*2*1
##8!=8*7*6*5*4*3*2*1
##n!=n*(n-1)*(n-2)*(n-3)* ... * 3*2*1
##n!=n*(n-1)!
##0!=1
##1!=1
def my_func(n):
    ##base case
    if n == 0 or n ==1:
        return 1
    else:
        return n * my_func(n - 1)
print("ex1",my_func(4))
## my_func(n)=n*my_func(n-1)
##     = n*(n-1)*my_func(n-2)
##
##
##     = n*(n-1)*my_func(n-2)... 3 *2*1*1
#ex2:
## 0 1 1 2 3 5 8 13 21 ...
#  فيبوناتشي
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
print("ex2",f(7))
## f(7)=f(6)+f(5)=f(5)+f(4)+f(4)+f(3)=
## = f(4)+f(3)+ f(3)+f(2)+f(3)+f(2)+f(2)+f(1)
## = f(3)+f(2)+f(2)+f(1)+f(2)+f(1)+f(1)+f(0)+f(2)+f(1)+f(1)+f(0)+f(1)+f(0)+1
## = f(2)+f(1)+f(1)+f(0)+f(1)+f(0)+1+f(1)+f(0)+1+1+0+f(1)+f(0)+1+1+0+1+0+1
## = f(1)+f(0)+12
##= 1+0+12=13

## Hasan Hajjar
## حسن حجار

## Lambda

## syntax
## lambda arguments:expression
##ex3
x=lambda a:a+8
print(x(3))
##ex4
x=lambda a,b:a+b
print(x(3,6))
##ex5
x=lambda a,b:a*b
print(x(3,6))

##ex6
def myfunc(n):
    return lambda a:a*n
doubler=myfunc(2) 
print(doubler(5))   
##ex7
def myfunc(n):
    return lambda a:a*n
ttriple=myfunc(3) 
print(ttriple(5))   

##ex8
def myfunc(n):
    return lambda a:a*n
doubler=myfunc(2) 
ttriple=myfunc(3) 
print(doubler(5)) 
print(ttriple(5))  

## arrays

## oop
## class 
## صنف - صف - فئة -فصل
## object

##create class 
class player:
    name="Guest"
    idd="guest"

## create object
player1=player()


## print prop
print(player1.name)

## __init__()

##create class 
class Player:
    name="Guest"
    idd="guest"
    def __init__(self,namee,iddd):
        self.name=namee
        self.idd=iddd

player1=Player("maan","manaf") 
print(player1.name)     
print(player1.idd)     