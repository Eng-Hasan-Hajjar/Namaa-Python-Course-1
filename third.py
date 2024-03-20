# أسماء صحيحة
mySubject="math"

myVariableName = "new"
MyVariableName = "new2"
my_variable_name = "husam"

# الإسناد لمتغيرات
x = 95
y = 90
z=80

x,y,z = 95 ,90 ,80 
print(x)
print(y)
print(z)
print(z,y)

# تعيين قيمة واحدة لعدة متغيرات
x=y=z= 98
print(x)
print(y)
print(z)
x=y=z= "maaan"
print(x)
print(y)
print(z)

fruits=["apple","banana","cherry"]
x,y,z=fruits
print(fruits)
print(x)
print(y)
print(z)
# print
x="python is awesome"
print(x)


x="python"
y="is"
z="awesome"
print(x,y,z)
# معامل الجمع للسلاسل والأرقام
x="python "
y="is "
z="awesome"
print(x + y + z)

x=5
y=6
print(x + y)

x="5"
y="6"
print(x + y)
# لايمكن الجمع بين العدد والسلسلة
x=5
y="abd fattah"
#print(x + y)

x=5
y="abd fattah"
print(x , y)

# المتغيرات العامة 

x="nice"

def myfunc():
    print("python is " + x)

myfunc()    


# example 2

x2="nice"

def myfunc2():
    x2="great"
    print("python is " + x2)

myfunc2()

print("python is " + x2)  

# global

def myfunc3():
    global x3
    x3="great"

myfunc3()

print("python is " + x3)

# global


def myfunc4():
    global x4
    x4="great4"

#print("python is 4" + x4)   

myfunc4()

# example 5
x5 ="nice"
def myfunc5():
    global x5
    x5="great5"

print("python is 5" + x5)   

myfunc5()


