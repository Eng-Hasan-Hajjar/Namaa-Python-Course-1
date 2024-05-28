"""
maan 46
Abd fattah  40
ismail 33
manaf 33
gith 25
sedra 22
jaber 21
obia 16
Bhaa 9
lama 3
hussam 2
ahmad  1

"""


"""
courses=("python","Security","English","computer icdl")
print(courses)

courses=("python","python","English","computer icdl")
print(courses)
courses=("python","Security","English","computer icdl")
print(len(courses))
courses=tuple(("python","Security","English","computer icdl"))
print(courses)
"""

##ex1
courses=("python")
print("ex1",courses)
print("ex1 type",type(courses))

##ex2
courses=("python","python","English","computer icdl")
print("ex2",courses)
print("ex2 type",type(courses))

##ex3
courses=("python",)
print("ex3",courses)
print("ex3 type",type(courses))


#ex4
##homework
courses=("python","python","English","computer icdl")
marks=(12,30,22,11)
suseces=(True,False,True,False)
print("ex4",courses)
print("ex4 type",type(courses[0:5]))
print("ex4",marks)
print("ex4 type",type(marks[0]))
print("ex4",suseces)
print("ex4 type",type(suseces[0]))

cor=(1,2,3,4,5)
for x in cor :
    print("ex4 maan",type (x))


## ex5
courses=("python",4,True,"computer icdl")

print("ex5",courses)

##ex6
courses=("python","python","English","computer icdl")
print("ex6",courses[2])


##manaf 
courses = ("python", "python", "English", "computer Icdl")

for course in courses:
    if course != "English":
        print("manaf",course)

##giath
courses = ("python", "python", "English", "computer icdl")

filtered_courses = []
for course in courses:
    if course != "English":
        filtered_courses.append(course)

print(filtered_courses)    

##ismail
courses=("python", "python", "English", "computer icdl")
courses2= "English"

for course in courses :
    if course != courses2:
        print("ismail",course)


##sedra
courses=("python", "python", "English", "computer icdl")

x= courses[:2]+ courses[3:]
print("sedra",x)  

## maan

courses = ("python", "python", "English", "computer icdl")
x = [x for x in courses if x != "English"]
print(x)

## abdfattah

courses=("python","python","English","computer icdl")
newcourse=[x for x in courses if x != "English"]
print(newcourse)

##ex7
courses=("python","python","English","computer icdl")
print("ex7",courses[2:])

##ex8
courses=("python","degango","flask","machin learning","al",
"mobile app","games","data analys")
print("ex8",courses[-1])

##ex9
courses=("python","degango","flask","machin learning","al",
"mobile app","games","data analys")
print("ex9",courses[-3])

##ex10
courses1=("python","degango","flask","machin learning","al")

courses2=("mobile app","games","data analys")


courses=courses1+courses2
print("ex10",courses)

##ex11
courses1=("python","degango","flask","machin learning","al")
#courses2=("games",)
courselist=list(courses1)
courselist.append("games")
courses1=tuple(courselist)
print("ex11",courses1)


##ex12
courses1=("python","degango","flask","machin learning","al")
courses2=("games",)
courses1+=courses2 ## courses1=courses1+courses2

print("ex12",courses1)


##ex13
courses1=("python","degango","flask","machin learning","al")
courselist=list(courses1)
courselist.remove("flask")
courses1=tuple(courselist)
print("ex13",courses1)







































