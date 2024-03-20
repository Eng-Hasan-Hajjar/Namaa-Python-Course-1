# example 6  مراجعة واختبار
x5 ="nice"
def myfunc5():
    global x5
    x5="great5"

print("python is 5" + x5)   

myfunc5()

print("python is 5" + x5) 


##  أنواع البيانات 
## int - float - string - complex 
## list - tuple - range -
## dict القواميس 
## set frozenset 
## bool القيم البوليانية المنطقية
## bytes memoryview 
## NoneType

## الحصول على النوع 
## ex 1

x=5
print(type(x))

# ex 2
x="hello world"
print(x)
print(type(x))

# ex3 
y= 66.55
c=22
print(y,c)
print(type(y),type(c))

# ex 4 complex
## z= a + b j
## z= bj

g=1j
print(g)
print(type(g))

h=1+1j
print(h)
print(type(h))

h2=-6+5j
h2=6+5j

print(h2)
print(type(h2))

## ex5 
ops=-6.2
print(ops)
print(type(ops))
## ex6  - list
v=["apple","banana","tomato"]
print (v)
print (type(v))
## ex 7 - tuple
b=("apple","banana","tomato")
print (b)
print (type(b))

# ex 8  range
s=range(8)
print (s)
print (type(s))

#ex 9 القاموس
d={"name":"Omar","age":32}
print (d)
print (type(d))

# ex 10 set المجموعة
m={"apple","banana","tomato"}
print (m)
print (type(m))

# ex 11 frozenset 
m2=frozenset({"apple","banana","tomato"})
print (m2)
print (type(m2))

# ex 12 bool
kam=True
print(kam)
print(type(kam))
kam=False
print(kam)
print(type(kam))

## ex 13 error
#kamt=true
#print(kamt)
#print(type(kamt))

# ex 14 bytes 
r=b"hello"
print(r)
print(type(r))

# ex 15 bytearray
r2=bytearray(5)
print(r2)
print(type(r2))
## ضبط النوع 
# ex 16
f=str("Hasan")
print(f)
print(type(f))

# ex 17 
fx=int(5)
print(fx)
print(type(fx))

