## stars
## النجوم 
## عبد الفتاح
## مناف 
## ابي
## معن
## عبد الفتاح
## جابر
#######################################
## عبد الفتاح
## مناف 
## ابي
## معن
## اسماعيل
## جابر

## اسماعيل
## سيدرا

## الفرق بين lower() and casefold()

## capitalize()
## تحويل الحرف الأول الى حرف كبير
## مثال
txt="hello , and welcome to my world"
x=txt.capitalize()
print(x)

## ex 2
txt="hello , and welcome to my world"
x=txt.upper()
print(x)

## ex 3
txt="hello ,. and welcome to my WORlD"
x=txt.capitalize()
print(3,x)

## casefold()
## ex 4
txt="Hello , And Welcome To My World"
x=txt.casefold()
print(x)

## ex 5
txt="Hello , And Welcome To My World"
x=txt.lower()
print(x)

## الفرق بين lower() and casefold()

## center(length, char)
## ex6
## اطبع كلمة "banana"  بمساحة 20 حرفاً مع وضع كلمة "banana " في المنتصف

txt="banana"
x=txt.center(20)
print(x)

## ex7 
## اعد السؤال السابق ولكن بوضع الرقم 2 كحرف حشو
txt="banana"
x=txt.center(20,"2")
print(x)


## count() 
## count(value,start,end)
## value req(اجبارية)
## ارجاع عدد المرات التي تحدث فيها قيمة معينة في السلسلة
## ex8
## اطبع عدد المرات التي تظهر فيها القيمة 
## "apple"
## في السلسلة 
## "I love apples , apples are my favrite fruit"

txt="I love apples , apples are my favrite fruit"
x=txt.count("apple")
print(8,x)
## ex 9
txt="I love apples , apples are my favrite fruit - apple"
x=txt.count("apple")
print(9,x)

## ex 10------------------
## البحث  (عددهم)عن قيمة معينة 
##  apple
## من الموضع 10  الى 24
##"I love apples , apples are my favrite fruit - apple"

txt="I love apples , apples are my favrite fruit - apple"
x=txt.count("apple",10,24)
print(10 ,x)

## ex11
txt="I love apples , apples are my favrite fruit - apple"
x=txt.count("apple",10)
print(11 ,x)

## ex12
txt="I love apples , apples are my favrite fruit - apple"
x=txt.count("apple",0 ,24)
print(12 ,x)


## find()
## يبحث عن قيمة معينة في السلسلة ويعيد الموضع الذي تم العثور عليه
#ex13
## أين توجد في النص التالي كلمة "apple" 
# "I love apples , apples are my favrite fruit - apple"

txt="I love apples , apples are my favrite fruit - apple"
x=txt.find("apple")
print(13 , "find ()" ,x)
## ex14
txt="I love apples , apples are my favrite fruit - apple"
x=txt.find("manaf")
print(14 , "find ()" ,x)

## find(value,start , end)
## value --- required
## ex15
txt="I love apples , apples are my favrite fruit - apple"
x=txt.find("m")
print(15 , "find ()",x )