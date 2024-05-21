
## abdfattah *4
## maan *4 
## jaber * 6
## lama *2
## manaf * 3
## ismail * 3
## giath * 2
## sedra *2
## 
## 

## list 
## review 15
oopp=["gamal","ahmad","adnan"]
print(oopp)

pprr=list(("manaf","ismail","sedra","lama"))
print(pprr)

##ex1
## تكرار القيم بالقائمة 
##
names=list(("manaf","ismail","sedra","ismail"))
print(names)


##ex2 
## عدد العناصر في القائمة
names=list(("manaf","ismail","sedra","ismail"))
print(len(names))

## اكتب برنامج يقوم بطباعة أسماء الطلاب الحضور
## ثم يقوم البرنامج بفص عدد الطلاب اذا كان أكبر من 5 طلاب يقةم البرنامج طباعة رسالة شكر للطلاب
## واذا لم يكن كذلك نطبع رسالة نتمنى الحضور من الجميع 

##ex3 
## types of list

names=list(("manaf","ismail","sedra","lama"))
stars=["5","6","3","0"]
stars=[5,6,3,0]
evalution=["true","true","true","false"]
evalution=[True,True,True,False]
print(len(names))
print(stars)


##ex4 
names_stars=["manaf",5,True,"ismail",6]


##ex5
print("ex5...............",names_stars)
print(names_stars[0])
print(names_stars[1])
print(names_stars[2])

##ex6
print("ex6...............",names_stars)
print(names_stars[-1])
print(names_stars[-2])
print(names_stars[-3])

## abdfattah

attended_students=["A","B","C","D","E","F"]
print("Students who attended the lesson",attended_students)
if len(attended_students) > 5:
    print("abdfattah","Thank you for attending this lesson")
else:
    print("abdfattah","Please attend the lesssons as scheduled")

## manaf

present_students = ["Manaf", "Ismaeil", "Lama", "Jaber", "Sedra", "Abd alfatah", "Maan", "Gaith"]

# طباعة أسماء الطلاب الحاضرين
print("أسماء الطلاب الحاضرين:")
for student in present_students:
        print(student)

# فحص عدد الطلاب
if len(present_students) > 5:
        print("شكراً لحضوركم جميعاً!")
else:
        print("نتمنى الحضور من الجميع")


## gaith
students_present = ["مناف", "اسماعيل", "معن", "سارة", "احمد", "نور"]
def print_attendance(students):
    print("قائمة الحضور:")
    for student in students:
        print(student)

def check_attendance(students):
    if len(students) > 5:
        print("شكراً لحضوركم جميعاً")
    else:
        print("نأمل حضور الجميع") 

print_attendance(students_present)
check_attendance(students_present)        

##maan
names=["ismail","sedra","maan","jaber","manaf","abd alfattah"
       ,"hussam","obai","hith","bhaa","lama","ahmad"]
print(names)
if len(names)>5:
    print("شكرا للطلاب الحضور")
else:
    print("نتمنى الحضور من الجميع")
##ismail
students= ["manaf" , "ghaith" , "abdulfattah" , "jaber" , "maan" , "sedra" , "lama" , "ismail"]

print (students) 

if len(students) > 5:
    print("شكراً للطلاب الحضور")
else:
    print("نتمنى الحضور من الجميع")

##    jaber
# 
students = ["جابر", "معن", "مناف", "عبد الفتاح", "سدرة", "اسماعيل"]


print(" students")
for student in students:
    print(student)


num_students = len(students)


if num_students > 5:
    print("شكراً لحضوركم جميعاً")
else:
    print("نأمل حضور الجميع في القادم") 

##    
##ex7
names=["ismail","sedra","maan","jaber","manaf","abd alfattah"
       ,"hussam","obai","hith","bhaa","lama","ahmad"]
print("ex7",names[2:4])

##ex8
names=["ismail","sedra","maan","jaber","manaf","abd alfattah"
       ,"hussam","obai","hith","bhaa","lama","ahmad"]
print("ex8",names[0:5])
print("ex8",names[:5])
print("ex9",names[4:])

##ex9
names=["ismail","sedra","maan","jaber","manaf","abd alfattah"
       ,"hussam","hith","bhaa","lama","ahmad"]

if "obia" in names:
    print("obia exist here")  
else :
    print("obia not here")     

##
#ex10
names=["ismail","sedra","maan","jaber","manaf","abd alfattah"
       ,"hussam","hith","bhaa","lama","ahmad"] 
print(names)    
names[7]="gaith"
print(names)   

##ex11
names=["ismail","sedra","aan","aber","anaf","abd alfattah"
       ,"hussam","hith","bhaa","lama","ahmad"] 
print(names)   
names[2:5]=["maan","jaber","manaf"]       
print(names)  


##ex12 
## تبديل قيمة عنصر بقيمتين 
cars=["bmw","ford","marcedece"]
print(cars)   
cars[1:2]=["ford1","ford2"]       
print(cars)  
##ex13
## تبديل قيمة عنصر بثلاثة قيم 
cars=["bmw","ford","marcedece"]
print(cars)   
cars[1:2]=["ford1","ford2","ford3"]       
print(cars) 

##ex14
## تبديل قيمة عنصر بقائمة فيها ثلاثة قيم 
cars=["bmw","ford","marcedece"]
print(cars)   
cars[1]=["ford1","ford2","ford3"]       
print(cars) 

## jaber
x=[1,2,3]
y=[1,2,3]
x=y
print (x is y) #False
print (x is x) #True
print (x is not y) #True


my_list=[1,2,3,4,5]
print (3 in my_list)#T
print (6 in my_list)#F

print (3 not in my_list)#F
print (6  not in my_list)#T


#in #not in
#ex1
mylist=[1,2,3,4,5]
print("ex1",3 in mylist)
print("ex1",6  in mylist)
print("ex1",3 not in mylist)
print("ex1",6 not in mylist)

#ex2
x=y=z=5
x=2
y=3
print("ex2",x is y)
print("ex2",x is not y)
print("ex2",x is z)

print("ex2",x is not z)
## ismail
f = ["ford", "bmw", "dodge"]
s = ["ford", "bmw", "dodge"]
z = f

print(f is z)
#
print(f is s)
##############
f = ["ford", "bmw", "dodge"]
s = ["ford", "bmw", "dodge"]
z = f
print(f is  s)

print(f is not s)
#####################
f = ["ford", "bmw", "dodge"]
print("ford" in f)

print("bmw" not in f)




#is , is not:
#هما معاملان لمقارنة قيم المتحولات في الذاكرة
#ex1: is
x=2
y=2
z=3
print("ex1",x is y)
print("ex1",x is z)
#ex2: isnot
x=2
y=2
z=3
print("ex2",x is not z)
print("ex2",x is not y)
# in , not in:
#هما معاملان للتحق من وجود قيمة داخل تسلسل مثل
#list , tuple , set , str
#ex3: in
ls=[1,2,3]
print("ex3",3 in ls)
print("ex3",5 in ls)
#ex4: not in
ls=[1,2,3]
print("ex4",5 not in ls)
print("ex4",3 not in ls)


## 
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