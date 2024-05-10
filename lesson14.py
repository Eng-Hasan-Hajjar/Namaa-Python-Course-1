



## oubia  *4
## manaf *6
## ismail *6 
## giath *6
## maan *6
## sedra * 5
## abd fattah * 5
## ahmad 







## المعاملات الإسنادية
 ## =
 ## +=
 ## -=
 ## *=
 ## /=
 ## %=
 ## //=
 ## **=
 ## ex1

x=10
y=5
z=3.5
g=12
h=4
print("x=10 ,y=5, z=3.5 , g=12 ,h=4 ")
x+=y
y+=x
## x=x+y
print("ex1 :x=x+y","x (new) =" ,x)
## ex2
print("ex2 :y=y+x","y (new) =" ,y)
z-=x
## ex3
print("ex3 :z=z-x","z (new) =" ,z)

## ex4

h*=y
print("ex4 :h=h*y","h (new) =" ,h)


## ex5

y/=4
print("ex5 :y=y/4","y (new) =" ,y)


## ex6

y=24
y//=g
print("ex6 :y=y//g","y (new) =" ,y)


## ex7

y=4
g=2
y**=g
print("ex7 :y=y**g","y (new) =" ,y)



## معاملات المقارنة
##يساوي
## ==
##لايساوي
## !=
##هل أكبر تماما
## >
## <
## >=
## <=



## ex8

if y==g :
    print("ex8 :y=g","if true " ,"y=",y ,"g=", g)
else :
    print("ex8 :y!=g","if false " ,"y=",y ,"g=", g)

## ex9

if y!=g :
    print("ex9 :y!=g","if true " )
    print("y=",y ,"g=", g)
else :
    print("ex9 :y=g","if false " )
    print("y=",y ,"g=", g)

   
## ex10

if y>g :
    print("ex10 :y>g","if true " )
    print("y=",y ,"g=", g)
else :
    print("ex10 :y<g","if false " )
    print("y=",y ,"g=", g)

## ex11
g=16
if y>=g :
    print("ex11 :y>=g","if true " )
    print("y=",y ,"g=", g)
else :
    print("ex11 :y<g","if false " )
    print("y=",y ,"g=", g)


## ex12
g=16
if y<=g :
    print("ex12 :y<=g","if true " )
    print("y=",y ,"g=", g)
else :
    print("ex12 :y>g","if false " )
    print("y=",y ,"g=", g)


## ex13
g=64
if y<=g :
    print("ex13 :y<=g","if true " )
    print("y=",y ,"g=", g)
else :
    print("ex13 :y>g","if false " )
    print("y=",y ,"g=", g)

## المعاملات المنطقية
# and
# or
# not    

## ex14
y=10
g=15
x=5
u=6
if y<=g and x<u:
    print("ex14 :y<=g and x<u","if true " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)
else :
    print("ex14 :y>g and x<u","if false " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)


    
## ex15
y=10
g=15
x=5
u=6
if y<=g and x>u:
    print("ex15 :y<=g and x<u","if true " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)
else :
    print("ex15 :y>g and x<u","if false " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)


        
## ex16
y=10
g=15
x=5
u=6
if y<=g or x>u:
    print("ex16 :y<=g or x<u","if true " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)
else :
    print("ex16 :y>g or x<u","if false " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)

## ex17
y=10
g=15
x=5
u=6
if y>=g or x>u:
    print("ex17 :y<=g or x<u","if true " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)
else :
    print("ex17 :y>g or x<u","if false " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)

## ex18
y=10
g=15
x=5
u=6
if not y>=g :
    print("ex18 :y<=g or x<u","if true " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)
else :
    print("ex18 :y>g or x<u","if false " )
    print("y=",y ,"g=", g)
    print("x=",x ,"u=", u)


