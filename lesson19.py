
"""
maan 42
Abd fattah  36
ismail 31
manaf 27
gith 23
sedra 22
jaber 21
obia 16
Bhaa 9
lama 3
hussam 2
ahmad  1

"""
## short hand with expresion
## ex1
office = ["word", "excel", "power point","access"]
newlist2 = [x.upper() for x in office ]
print(newlist2)


## ex2
## قيمة ثابتة لجميع العناصر 

office = ["word", "excel", "power point","access"]
newlist2 = ['microsoft' for x in office ]
print(newlist2)

## ex3
## قيمة ثابتة لجميع العناصر 
##بشرط
office2 = ["word","ismail", "excel", "power point","access"]
newlist2 = ['microsoft' for x in office2 if x != "ismail"  ]
print("ex3",newlist2)

## ex4
## أرجع قيمة فيزو بدل اسماعيل
## قيمة بدل قيمة 

office = ["word","ismail", "excel", "power point","access"]
newlist2 = [x if x != "ismail" else "visio" for x in office   ]
print("ex4",newlist2)

## gaith
office = ["word", "ismail", "excel", "power point", "access"]
newlist2 = []

for x in office:
    if x != "ismail":
        newlist2.append(x)
    else:
        newlist2.append("visio")

print("gaith",newlist2)


## maan

office=["word","ismail","excel","power point","access"]
newlist=[]
for x in office:
    if x !="ismail":
        newlist.append(x)
    else :
        newlist.append("visio")
print("maan",newlist)

## abd fattah
office = ["word","ismail", "excel", "power point","access"]
newlist2 =[]
for x in office:
    if x != "ismail":
        newlist2.append(x)
    else:
     newlist2.append("vision")
 
print(newlist2)

##sedra 
office = ["word", "ismail", "excel", "power: point", "access"]
newlist2 = []

for x in office:
    if x == "ismail":
        newlist2.append("visio")
    else:
        newlist2.append(x)

print(newlist2)

#oubai
office = ['word','oubai','excel','power point','access']
newlist2 = []
for x in office:
    if "!= oubai" in x  :
        newlist2.append(x) 
    else :
        newlist2.append(x)
print(newlist2)


## ex5
office = ["word","ismail", "excel", "power point","access"]
office.sort()
print(office)


## ex6
officenum = [1,2,3,5,-8,-6,-1,0]
officenum.sort()
print(officenum)

## ex7
officenum = [1,2,3,5,-8,-6,-1,0]
officenum.sort(reverse=True)
print(officenum)

## custumize
## ex8
## اكتب برنامجا لترتيب الأعداد وقفا لمدى قربها من ال 50
def myfun(n):
    return abs(n-50)

numlist=[100,50,65,82,23,1]
numlist.sort(key=myfun)
print(numlist)


## ex9
## حساسية الأحرف مع الفرز 
## الأحرف الكبيرة قبل الصغيرة
office = ["word", "excel", "Power point","Access"]
office.sort()
print(office)


## ex10
## حساسية الأحرف مع الفرز 
## الأحرف الكبيرة قبل الصغيرة
office = ["word", "excel", "Power point","Access"]
office.sort(key=str.lower)
print(office)


## ex11
office = ["word", "excel", "power point","access"]
office.sort()
print(office)
office.reverse()
print(office)

## ex12
## copy()
office = ["word2", "excel", "power point","access"]
office2=office.copy()

print(office)

print(office2)
## ex13
## list()
office = ["word3", "excel", "power point","access"]
office2=list(office)

print(office)

print(office2)
## ex14

office = ["word4", "excel", "power point","access"]
office2=office

print(office)

print(office2)

## ex15
## join list
office1 = ["word4", "excel"]
office2 = [ "power point","access"]
office3=office1+office2

print(office1)

print(office2)
print(office3)

## ex16
## join list
##extend()
office1 = ["word4", "excel"]
office2 = [ "power point","access"]
print(office1)
print(office2)
office1.extend(office2)
print(office1)
print(office2)


## ex17
## join list
##append()
office1 = ["word4", "excel"]
office2 = [ "power point","access"]

for x in office2:
    office1.append(x)

print(office1)


## tuples
courses=("python","Security","English","computer icdl")
print(courses)

## tuples
courses=("python","python","English","computer icdl")
print(courses)
## ex14
courses=("python","Security","English","computer icdl")
print(len(courses))
## ex15
courses=tuple(("python","Security","English","computer icdl"))
print(courses)