"""
maan 47
Abd fattah  42
ismail 33
manaf 34
gith 26
sedra 22
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














































































