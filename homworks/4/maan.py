h= str ("Hello world")
print (h)
print (type(h))
Number_of_students=range(100)
print(Number_of_students)
print(type (Number_of_students))
lessons= dict({"python" :10,"English":15,"math" :20})
print(lessons)
print (type(lessons))
students={"ahmed","omar","ali","muhammed"}
print(type(students))
python= {40,25,61,15}
a,b,c,d=python
def mark():
    global m 
    m= 60
    x=True
    y=False
    if a > m:
        print("ahmed",a,x,"ناجح")
        print(type(x))
    if a < m:
        print("ahmed",a,y,"راسب")
        print(type(y))
mark()