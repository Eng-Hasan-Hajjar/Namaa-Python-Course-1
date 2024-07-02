"""
maan 61
Abd fattah  68
ismail 51
manaf 50
gith 46
sedra 49
jaber 21
obia 16
Bhaa 9
lama 3
hussam 2
ahmad  1

"""


##functions
def my_func():
    print("hello world")
my_func()


## arguments
## الوسيطات
def my_func2(fname):
    print(fname + " rafi")

my_func2("Emily")   

my_func2("tobias")  

##num of arguments
def my_func3(fname ,lname):
  print(fname+" "+lname)  

my_func3("hasan","hajjar")
#my_func3("bahaa") ## error
## الوسطاء التعسفية
def my_func4(*players):
    print("pubg"+ players[2])

my_func4("Emily","Vic","Elthabith")   
