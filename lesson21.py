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


##ex1
## del

courses1=("python","degango","flask","machin learning","al")
del courses1

##print("ex1",courses1)


## ex2
courses1=("python","degango","flask")
sub1=courses1[0]
sub2=courses1[1]
sub3=courses1[2]
print("ex2",sub1,sub2,sub3)


## ex3
courses2=("python","degango","flask")
(sub1,sub2,sub3)=courses2

print("ex3",sub1,sub2,sub3)


## ex4
courses2=("python","degango","flask","machin learning","al")
(sub1,*sub2,sub3)=courses2

print("ex4",sub1,sub2,sub3)

## ex5
courses2=("python","degango","flask","machin learning","al")
(sub1,sub2,*sub3)=courses2

print("ex5",sub1,sub2,sub3)

## ex6
courses2=("python","degango","flask","machin learning","al")
(*sub1,sub2,sub3)=courses2

print("ex6",sub1,sub2,sub3)

## ex7
courses=("python","degango","flask","machin learning","al")
for x in courses:
    print("ex7",x)

## ex8
courses=("python","degango","flask","machin learning","al")
for i in range(len(courses)):
    print("ex8",courses[i])


## ex9
courses=("python","degango","flask","machin learning","al")
i=0
while(i<len(courses)):
    print("ex9",courses[i])
    i=i+1
    #i+=1

## ex10
courses=("python","degango","flask","machin learning","al")
courses2=("python2","degango2","flask2","machin learning2","al2")
courses3=courses+courses2

print("ex10",courses3)

## ex11
courses=("python","degango","flask","machin learning","al")
courses3=courses*2

print("ex11",courses3)

## ex12
courses=("python","degango","flask","machin learning","al")
courses3=courses*3

print("ex12",courses3)

## ex13
courses=("python","python","python","machin learning","al")

x=courses.count("python")
print("ex13",x)

## ex14
marks=(5,6,7,8,8,7,4,5,4,7,3,2,1,4,2)

x=marks.count(5)
print("ex14",x)


##abdfattah
marks=[1,2,3,4,4,5,5,5,6,6,6,7,8,8,9,9,9,9]
marks=(5,6,7,8,8,7,4,5,4,7,3,2,1,4,2)
for x in set(marks):
    print("abd fattah",x,marks.count(x))

##manaf
# 
marks=(1,2,2,3,4,4,5,5,5)
for x in marks:
        print("manaf",x,marks.count(x))    

marks=(1,2,2,3,3,4,4,5,5,5)
for x in marks:
    print(x)


##maan
marks=(5,6,7,8,8,7,4,5,4,7,3,2,1,4,2)
dic = {}
for i in marks:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i, count in dic.items():
    print(f"{i}: {count}")

## giath
marks = (5, 6, 7, 8, 8, 7, 4, 5, 4, 7, 3, 2, 1, 4, 2)
unique_marks = (marks)
for mark in unique_marks:
    count = marks.count(mark)
    print("giath",f"{mark}: {count}")


## ex15
marks=(3,6,7,8,8,7,4,5,4,7,3,2,1,4,2)

x=marks.index(5)
print("ex15",x)

## الفرق بين 
## procedure
## method
## functions


#
## set 
## المجموعات

##ex16
courses={"python","ai","machin learng","math","Algabra","dev","suface","tensorflow"}
print("ex16-1",courses)
print("ex16-2",courses)

##ex17
courses=set(("python","ai","machin learng","math","Algabra","dev","suface","tensorflow"))
print("ex17",type(courses))

##ex18
courses=set(("python","python","machin learng","python","Algabra","dev","suface","tensorflow"))
print("ex18",courses)
##ex19
courses=set(("python","python","machin learng","python","Algabra","dev","suface","tensorflow"))
print("ex19",len(courses))


##ex20
courses=set(("python","python","machin learng",True,"Algabra","dev","suface","tensorflow"))
print("ex20",courses)


##ex21
courses=set(("python","python","machin learng",True,1,5,"suface","tensorflow"))
print("ex21",courses)

##ex22
courses=set(("python","python","machin learng","surface","tensorflow"))
for x in courses:

    print("ex22",x)

##ex23
courses=set(("python","python","machin learng","surface","tensorflow"))
for x in courses:
      print("ex23","surface" == x)

##ex24
courses=set(("python","python","machin learng","surface","tensorflow"))

print("ex24","surface" in courses)




