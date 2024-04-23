"""
إسماعيل 7
سيدرا 4
معن 10
جابر 6
مناف 5
عبد الفتاح 6
حسام 2
أُبي 4
غيث 3
بهاء 8

"""
## adb fattah *3
## ismail *3
## manaf 
## jaber
## bha
## maan
## 


## join()
## string.join(iter)
## iter req
## يربط عناصر التكرار حتى نهاية السلسلة

##ex1
## قم بربط جميع العناصر الموجودة في تيوبل في سلسلة باستخدام حرف التجزئة كفاصلة
mytuple=("Abd","jaber","ismail")
x=" ,".join(mytuple)
print(1,"join()",x)

##ex2
## قم بربط جميع العناصر الموجودة في تيوبل في سلسلة باستخدام حرف التجزئة ك 
## ++
mytuple=("Abd","jaber","ismail")
x=" ++".join(mytuple)
print(2,"join()",x)



## ex3
## with dic
myDic={"name":"Bha","country":"Syria"}
mySeprtor="TEST"
x=mySeprtor.join(myDic)
print(3,"join()",x)


## splitlines()
## يقسم السلسلة عند فواصل الأسطر ويعيد قائمة
##ex4
txt="Hello , welcome\n to our course."
x=txt.splitlines()
print(4 , "splitlines ()",x)

## string.splitlines()
## وظفية 

## startswith()
## يرجع قيمة صحيحة اذا بدأت السلسلة بالقيمة  المحددة
## startswith(value ,start ,end)
## value req

# ex5
txt="Hello , welcome to our course."
x=txt.startswith("Hello")
print(5 , "startswith ()",x)

# ex6
txt="Hello , welcome to our course."
x=txt.startswith("welcome")
print(6 , "startswith ()",x)

# ex7
txt="Hello , welcome to our course."
x=txt.startswith("welcome")
print(7 , "startswith ()",x)

# ex8
txt="Hello , welcome to our course."
x=txt.startswith("welcome",8,19)
print(8 , "startswith ()",x)

# ex9
txt="Hello , welcome to our course."
x=txt.startswith("welcome",5,20)
print(9 , "startswith ()",x)

## swapcase()
## string.swapcase()

## يبدل الأحرف الصغيرة بالكبيرة والكبيرة بالصغيرة


# ex10
txt="Hello , welcome to our course."
x=txt.swapcase()
print(10 , "swapcase ()",x)

# ex11
txt="Hello , welcome to our course."
x=txt.swapcase()
#x=txt.swapcase(8,19)
print(11 , "swapcase ()",x)

## اكتب برنامج يقوم ب تحويل الحرف الصغير الى كبير والعكس ولكن ضمن مجال محدد مثلا بين 
## [8-19]
## بالاعتماد على ما أخذناه
## الجواب الصحيح ب 2 نجمة

## ###############
## title()
## string.title()
## تحويل الحرف الأول من كل كلمة الى أحرف كبيرة
## ex12
txt="Hello , welcome to our course."
x=txt.title()
print(12 , "title ()",x)


## القيم البوليانية المنطقية 

## ex 13
print(13-1,10>9)
print(13-2,10==9)
print(13-3,10<9)

## ex 14
print("13-1",10>9)
print("13-2",10==9)
print("13-3",10<9)

