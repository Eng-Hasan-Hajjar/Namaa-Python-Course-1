"""
maan 48
Abd fattah  44
ismail 34
manaf 37
gith 27
sedra 25
jaber 21
obia 16
Bhaa 9
lama 3
hussam 2
ahmad  1

"""

## add in set
##ex1
A={"python","machin","surface","tensorflow"}
B={"python2","machin2","surface2","tensorflow2"}
A.update(B)
print("ex1 A", A)

print("ex1 B", B)

##ex2
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}
A.update(B)
print("ex2 A", A)

print("ex2 B", B)
## add list to set 
##ex3
A={"python","machin","surface","tensorflow"}
B=["python","machin","surface2","tensorflow2"]
A.update(B)
## B.update(A)##error
print("ex3 A", A)

print("ex3 B", B)
##delete elements
##ex4
A={"python","machin","surface","tensorflow"}
print("ex4 A", A)
A.remove("machin")
print("ex4 A", A)

##delete elements with error
##ex5
A={"python","machin","surface","tensorflow"}

A.remove("machin")
print("ex5 A", A)

##discard elements 
##ex6
A={"python","machin","surface","tensorflow"}

#A.discard("machin2")
print("ex6 A", A)


##discard elements 
##ex7
A={"python","machin","surface","tensorflow"}

A.discard("machin2")
print("ex7 A", A)


##pop() 
##ex8
A={"python","machin","surface","tensorflow"}

A.pop()
print("ex8 A", A)



##pop() 
##ex9
A={"python","machin","surface","tensorflow"}
popelement=A.pop()
print("ex9 popelement", popelement)
print("ex9 A", A)

##clear() 
##ex10
A={"python","machin","surface","tensorflow"}
A.clear()
print("ex10 A", A)


##del 
##ex11
A={"python","machin","surface","tensorflow"}
del A
## print("ex11 A", A)

##for 
##ex12
A={"python","machin","surface","tensorflow"}
for x in A:
    print("ex12 x", x)
print("ex12 A", A)


## union()
##ex13
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}

C=A.union(B)
print("ex13 A ", A)
print("ex13  B", B)
print("ex13 A | B", C)


## | 
##ex14
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}

C=A | B
print("ex14 A ", A)
print("ex14  B", B)
print("ex14 A | B", C)


## union()
##ex15
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}
D={"python3","machin3","surface3","tensorflow3"}
C=A.union(B,D)
## C=A | B | D
print("ex15 A ", A)
print("ex15  B", B)
print("ex15  B", D)
print("ex15 A | B | D", C)




## intersection()
## التقاطع 
##ex16
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}

C=A.intersection(B)
## C=A & B
print("ex16 A ", A)
print("ex16  B", B)
print("ex16 A & B ", C)


## intersection_update()
## التقاطع 
##ex17
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}
print("ex17 A ", A)
print("ex17  B", B)
A.intersection_update(B)
print("ex17 A ", A)
print("ex17  B", B)


## intersection_update()
## التقاطع 
##ex18
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}
print("ex18 A ", A)
print("ex18  B", B)
#A.intersection_update(B)
A&=B
#A=A&B
print("ex18 A ", A)
print("ex18  B", B)


## difference()
## الفرق 
##ex19
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}

C=A.difference(B)
C=A-B

print("ex19 A ", A)
print("ex19  B", B)

print("ex19  C", C)


## difference()
## الفرق 
##ex20
A={"python","machin","surface","tensorflow"}
B=["python","machin","surface2","tensorflow2"]

C=A.difference(B)
#C=A-B

print("ex20 A ", A)
print("ex20  B", B)

print("ex20  C", C)




## difference_update()
## الفرق 
##ex21
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}

A.difference_update(B)
## A=A-B
print("ex21 A ", A)
print("ex21  B", B)



## symmetric_difference_update()
##ex22
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}

A.symmetric_difference_update(B)
## A=A^B
## A={A-B &  B-A}
print("ex22 A ", A)
print("ex22  B", B)





## symmetric_difference_update()
##ex23
A={"python","machin","surface","tensorflow"}
B={"python","machin","surface2","tensorflow2"}
C=A.symmetric_difference(B)
## C=A^B

print("ex23 A ", A)
print("ex23  B", B)

print("ex23  C", C)








































