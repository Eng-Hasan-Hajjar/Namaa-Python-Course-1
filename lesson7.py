## النجوم
## مناف 
## اسماعيل
## سيدرة
## عبد الفتاح

##المسافة البيضاء
## ex 1
txt="  Hello world! "
print(txt)
## ex2
txt2="Hello world! "
print(txt2)

## ex3 strip()
##المسافة البيضاء هي المسافة قبل و/أو بعد النص الفعلي، وفي كثير من الأحيان تريد إزالة هذه المسافة.
txt3="  Hello world! "
print(txt3.strip())


## replace() تابع الاستبدال
txt4="Hello world!"
print(txt4.replace("H","T"))

## ex 2
txt5="Hello world!"
print(txt5.replace("w","T"))

## ex 3

txt6="Hello world!"
print(txt6.replace("l","T"))

## split()
## التقسيم
txt7="Hello world!"
print(txt7.split())

## ex2
txt8="Hello , world!, Hello , world!"
print(txt8.split(","))

## ex3
txt9="Hello , world!"
print(txt9.split("o"))

## دمج السلاسل
a="Hello"
b="world"
c=a+b
print(c)

## ex2
a="Hello "
b="world "
c=a+b
print(c)

## ex3 طريقة أخرى للمسافة البيضاء ضمن السلاسل
a="Hello"
b="world"
c=a + " " + b
print(c)

## تنسيق السلاسل
age=28
#txt="My name is Hasan, I am " + age
#print(txt)

## format()
age=28
txt10="My name is Hasan, I am {} "
print(txt10.format(age))

## ex2 
quantity=2
itemNo=567
price=49.95
myOrder= "I want {} kg of item {} for {} SYP"
print(myOrder.format(quantity,itemNo,price))

## ex3
quantity=2
itemNo=567
price=49.95
myOrder= "I want {0} kg of item {1} for {2} SYP"
print(myOrder.format(quantity,itemNo,price))

## ex4
quantity=2
itemNo=567
price=49.95
myOrder= "I want {2} kg of item {0} for {1} SYP"
print(myOrder.format(itemNo,price,quantity))


## رموز الممنوعة في السلاسل
#txt13="I want 2 kg of "item" 567 for 49.95 SYP"
txt13="I want 2 kg of \"item\" 567 for 49.95 SYP"
print(txt13)
## ex2
txt14="I want 2 kg of  \'item\' 567 for 49.95 SYP"
print(txt14)
## ex3
txt15="I want 2 kg of  \\item\\ 567 for 49.95 SYP"
print(txt15)
## ex4
txt16="I want 2 kg of  \item\ 567 for 49.95 SYP"
print(txt16)

## ex5
txt17="I want 2 kg of  \\\item\\\ 567 for 49.95 SYP"
print(txt17)

## ex6 
txt18="I want 2 kg of  \n item  567 for 49.95 SYP"
print(txt18)

## ex7 
txt19="I want 2 kg of  \t item  567 for 49.95 SYP"
print(txt19)
