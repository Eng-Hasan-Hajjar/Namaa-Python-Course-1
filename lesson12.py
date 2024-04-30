"""
إسماعيل 10
سيدرا 4
معن 11
جابر 7
مناف 6
عبد الفتاح 9
حسام 2
أُبي 4
غيث 3
بهاء 9

"""
## abd fattah *4
## maan *4
## ismail *2
## oubia 1
## sedra 1
## jaber 2

## upload into github
"""
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Eng-Hasan-Hajjar/course-test.git
git push -u origin main

"""

## القيم البوليانية
## ex1
print("1-1",10>9)
print("1-2",10==9)
print("1-3",10<9)

## ex2
## اطبع رسالة بنا ء ً على شرط معين
a=200
b=33
if b>a :
    print("2 ex if = true" )
else:
    print("2 ex  if = false" )
##  او رقم
# تقييم سلسلة 
## ex3 
print("ex3",bool("Hello") )
print("ex3",bool(15) )

## اي سلسلة تقييمها صحيح الا السلسلة الفارغة
## اي رقم تقييمه صحيح الا العدد 0

## ex4

print("ex4",bool("") )
print("ex4",bool(0) )

## نفس الكلام بالنسبة لباقي المصفوفات 
## مثل القوائم او تيبلز أو القواميس 
## الا الفارغة منها 
## ex5

print("ex5- list",bool(["h","h","k"]) )
print("ex5- empty element list ",bool(["","",""]) )
print("ex5- empty list ",bool([]) )
print("ex5 - tuple",bool(("h","h","k")) )
print("ex5 - empty element tuple",bool(("","","")) )
print("ex5 - empty  tuple",bool(()) )


# function - return bool
## ex6

def jaber_Function() :
    return True

print("ex6",jaber_Function())    

##  (عبد الفتاح )اطبع (معن) اذا التابع أرجع قيمة صحيحة وإلا اطبع 

