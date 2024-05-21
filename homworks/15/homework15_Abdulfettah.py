#is
x=[1,2,3]
y=[1,2,3]
print("0" , x is y)


x1=[1,2,3]
y1=[1,2,3]
x1=y1
print("1" , x1 is y1)



#is not
x2=[1,2,3]
y2=[1,2,3]
print("2", x2 is not y2)


x3=[1,2,3]
y3=[1,2,3]
x3!=y3
print("3" , x3 is not y3)


#in / not in
text="Dealing something that must be done"
print("in" , "must be done" in text)
print("not in" , "must be done" not in text)