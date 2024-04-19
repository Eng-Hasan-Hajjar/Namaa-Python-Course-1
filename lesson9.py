## Ismail *2
## Maan * 5
## Bahaa *4
## sedra
## gaith
## manaf
##
## 
## ex1 

txt="I love apples , apples are my favrite fruit - apple"
x=txt.find("q")
print(1 , "find ()",x )

## index()
## اين توجد في النص 
## welcome
## Hello , welcome to our course

## ex2
txt="Hello , welcome to our course"
x=txt.index("welcome")
print(2 , "index ()",x )
## ex 3 
txt="Hello , welcome to our course"
x=txt.find("welcome")
print(3 , "find ()",x )

## index(value ,start ,end)
## value req اجبارية
## start , end  اختيارية
## ex 4
## اين يوجد في النص أول ظهور للحرف 
# e
 
txt="Hello , welcome to our course"
x=txt.index("e")
print(4 , "index ()",x )

## نفس المثال السابق ولكن ضمن المجال 5 و 10
## ex5 
txt="Hello , welcome to our course"
x=txt.index("e",5,10)
print(5 , "index ()",x)

## return exception استثناء 
## ex6
txt="Hello , welcome to our course"
x=txt.index("w",1,12)
print(6 , "index ()",x)


## endswith()
## يرجع قيمة صحيحة اذا انتهت السلسلة بالقيمة  المحددة
## endswith(value ,start ,end)
## value req

## ex7

txt="Hello , welcome to our course."
x=txt.endswith(".")
print(7 , "endswith ()",x)

## ex8
txt="Hello , welcome to our course."
x=txt.endswith("j")
print(8 , "endswith ()",x)

## ex9
txt="Hello , welcome to our course."
x=txt.endswith("e",5,10)
print(9 , "endswith ()",x)

## ex 10
txt="Hello , welcome to our course."
x=txt.endswith("our course.",5,10)
print(10 , "endswith ()",x)
## ex 11
txt="Hello , welcome to our course."
x=txt.endswith("our course.")
print(11 , "endswith ()",x)

## islower()

## ex12
txt="Hello , welcome to our course."
x=txt.islower()
print(12 , "islower ()",x)


## ex13
txt="hello , welcome to our course."
x=txt.islower()
print(13 , "islower ()",x)

## تحقق مما اذا كانت جميع الأحرف الموجودة في النص التالي صغيرة أو لا 
## ex14
a="hello 123"
b="myHasan"
aa=a.islower()
bb=b.islower()
print(14 , "islower ()",aa)
print(14 , "islower ()",bb)


## lstrip()
## يقوم ارجاع نسخة القطع اليسرى من السلسلة
## ex15
## ازل المسافات على القسم الأيسر من السلسلة
txt="            banana            "
print(15,"lstrp()" ,txt)
x=txt.lstrip()
print(15,"lstrp()" ,x)

## lstrip(char)
## char اختياري
## ex16
txt=",,,,,banana.....apple"
x=txt.lstrip()
print(16,"lstrp()" ,x)
## ex17
txt=",,,,,banana.....apple"
x=txt.lstrip(",.")
print(17,"lstrp()" ,x)

## ex18
txt=",,,,,.....banana.....apple"
x=txt.lstrip(",.")
print(18,"lstrp()" ,x)
## ex19
txt=",,,,,.....banana.....apple"
x=txt.lstrip(",")
print(19,"lstrp()" ,x)
## ex20
txt=",,,,,..aab...banana.....apple"
x=txt.lstrip(",.a")
print(20,"lstrp()" ,x)

## partition()
## تقوم بارجاع تيوبل حيث يتم تقسيم السلسلة الى ثلاثة أجزاء
# tuple = ("","","")
  
#ex 21
## ابحث عن كلمة 
## bananas
#وارجع تيوبل يحتوي على ثلاثة عناصر 
txt=",,,,,..aab...bananas.....apple"
x=txt.partition("bananas")
print(21,"partition()" ,x)
## partition(value)
## value req

## ex 22 
txt=",,,,,..aab...bananas.....apple"
x=txt.partition("yes")
print(22,"partition()" ,x)
## ex 23 
txt=",,,,,..aab...bananas.....apple"
x=txt.partition("apple")
print(23,"partition()" ,x)