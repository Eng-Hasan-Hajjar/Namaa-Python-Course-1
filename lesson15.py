"""
ismail 21
sedra 13
maan 25
jaber 12
manaf 17
Abd fattah  21
hussam 2
obia 13
gith 11
Bhaa 9
lama 1
ahmad  1

"""
## وظيفة
## معاملات أخرى
## is - is not
## in - not in



#####
## معاملات 
## الأسبقية
## مثال اكتب تعبيرا رياضيا بلغة البايثون
## يراعي موضوع الأسبقية للعمليات الرياضية 
## x = {2 * 5 -9 / 3 +(2^3)}

## ()
## **
## * / // % 
## + - 

## == != < > <= >= 

## is  is not in not in

## not  
## and
# or

## ex1
print("ex1", 5+4-7+3)
 
## ex2
print("ex2", 5+4*7+3)

## ex3
y=z=b=j=2 
y,z,b,n,j=2,2,1,1,2 
x= y * z + n * j / b ** 2 + (y+z)
print("ex3", x)


### tuple
## dic القاموس
## المجموعة set



## list 
## القوائم
##  هي عبارة عن مجموعة مرتبة وقابلة للتغيير وتسمح بتكرار الأعضاء أو العناصر

## انشاء القائمة
## ex4 
## create list
mylist=["hasan","ahmad","samer"]
print("ex4",mylist)
## ex5
## create list second method
mylist2=list(("hasan2","ahmad2","samer2"))
print("ex5",mylist2)
print("ex5",list(("hasan3","ahmad3","samer2")))

x=int(2)
print("ex5",x)
print("ex5",int(2))

## عناصر القائمة 
## مرتبة
## قابلة للتغيير
## تسمح بقيم مكررة

## #### مرتبة
## العنصر الأول دليله 0
## العنصر الثاني دليله 1

## اضافة العنصر الجديد يكون في آخر موضع



## قابلة للتغيير### 
## يمكن حذف أو اضافة أو تغيير العنصر أو العناصر 

## تسمح بقيم مكررة##
## يمكن أن تحتوي القائمة على عناصر متعددة بنفس القيمة

## ex6
## انشئ قائمة فيها قيم مكررة
mylist=["hasan","ahmad","samer","ahmad","samer","ahmad","samer"]
print("ex6",mylist)

## طول القائمة
## نستخدم التابع
## len()
## اطبع عدد العناصر بالقائمة 
## مثال
## ex7
mylist=["hasan","ahmad","samer","ahmad","samer","ahmad","samer"]
print("ex7",mylist ,len(mylist) )


## أنواع البيانات في القائمة
## ex8
mylist=["hasan","ahmad","samer"]
mylist2=[66,44,1]
mylist3=[True,False]
print("ex8",mylist ,len(mylist),type(mylist) )
print("ex9",mylist2 ,len(mylist2),type(mylist2) )
print("ex10",mylist3 ,len(mylist3) ,type(mylist3) )
print("ex11" ,type(mylist[0]),type(mylist[1]),type(mylist[2]) )
print("ex12" ,type(mylist2[0]),type(mylist2[1]),type(mylist2[2]))
print("ex13" ,type(mylist3[0]),type(mylist3[1])) 
