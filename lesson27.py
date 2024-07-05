"""
maan 77
Abd fattah  76
ismail 55
manaf 53
gith 48
sedra 52
jaber 21
obia 16
Bhaa 14
lama 3
hussam 2
ahmad  1

"""
## dict.setdefault()
## إذا كان المفتاح موجوداً يرجع قيمته
## إذا لم يكن موجوداً يدخل المفتاح بقيمة افتراضية ويرجع هذه القيمة
#ex1
d = {'a': 1}
value = d.setdefault('b', 2)
print(value) 
print(d)

## dict.fromkeys()
## ينشئ قاموساً جديداً من قائمة المفاتيح المحددة وقيمة افتراضية
#ex2
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

##ex1
## order of arguments
def my_func1(player1,player2,player3):
    print("pubg"+ player2)

my_func1(player3="Emily",player1="Vic",player2="Elthabith")   
my_func1("Emily","Vic","Elthabith")   

##ex2
## 
def my_func2(**players):
    print("pubg : "+ players["player2"])

my_func2(player3="Emily",player1="Vic",player2="Elthabith")   


##ex3
## 
def my_func3(**players):
    print("pubg : "+ players["player2"])

my_func3(player3="Emily",player1="Vic",player2="Elthabith")   

##ex4
## default parameter value
def my_func4(country="Europ"):
    print("he is from: "+ country)

my_func4("Syrian")
my_func4("India")
my_func4("Iraq")
my_func4("Germany")
my_func4()

##ex5
## 
def my_func5(equipments):
    for x in equipments:
        print(x)


equip=["gun","energy","scope","smoke","health"]


my_func5(equip)

##ex6
## 
def num_kill(x):
    return 5 * x

num=num_kill(3)
print(num)


##ex7
## 
def num_kill(x):
    pass 

def my_fuc10(x):
    print(x)

my_fuc10(x=3)

def my_fuc11(x,/):
    print(x)
##error
#my_fuc10(x=3)
def my_fuc12(x,/):
    print(x)

my_fuc10(3)


def my_fuc13(*,x):
    print(x)

my_fuc10(x=13)

def my_fuc14(*,x):
    print(x)
##error
##my_fuc14(14)

def my_fuc15(y,z,/,*,x):
    print(y+z+x)

my_fuc15(10,15,x=13)

## التعاودية
## وظيفة
## 5!=5*4*3*2*1


