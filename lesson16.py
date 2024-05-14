
## abdfattah *2
## maan *2 
## jaber *2 
## lama
## manaf * 2
## ismail
## giath


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

