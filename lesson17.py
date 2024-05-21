
"""
ismail 27
sedra 16
maan 33
jaber 21
manaf 24
Abd fattah  29
hussam 2
obia 13
gith 13
Bhaa 9
lama 3
ahmad  1

"""
# ex1
## قم بتغيير القيمة الثانية والثالثة باستبدالها بقيمة واحدة
laptops=["hp","asus","accer","del","sony","lenovo"]
print("ex1 before",laptops)
#laptops=["hp","asus","toshiba","sony","lenovo"]
laptops[2:4]=["toshiba"]
print("ex1 after",laptops)

## ex2
## ادراج عنصر
## insert()
laptops=["hp","asus","accer"]
print("ex2 before insert",laptops)
laptops.insert(2,"lenovo")
print("ex2 after insert" ,laptops)

## ex3
## اضافة عنصر الى نهاية القائمة
## append()
laptops=["hp","asus","accer"]
print("ex3 before append",laptops)
laptops.append("lenovo")
print("ex3 after append",laptops)

## ex4 
laptops=[400,500,350]
print("ex4 before append",laptops)
laptops.append(600)
print("ex4 after append",laptops)

## ex5 
## توسيع للقائمة
##extend()
types_sesions=["pss","pt","asd"]
not_forget_types_list=["referal","p and o"]

print("ex5 before extend()",types_sesions)
print("ex5 before extend()",not_forget_types_list)

types_sesions.extend(not_forget_types_list)

print("ex5 after extend()",types_sesions)
print("ex5 after extend()",not_forget_types_list)

## ex6
## توسيع للقائمة
##extend() with tuple
books=["demoq","madani","medicen"]
books_forget=("lebraria","islam")
print("ex6 before extend()",books)
books.extend(books_forget)
print("ex6 after extend()",books)

## معن
#sort()
print("maan ex sort ")
num=[7,5,6,2,1,10,25]
num.sort()
print(num)
labtops=["hp","lenovo","asus","toshiba"]
labtops.sort(key=len)
print(labtops)
#reverse()
labtops.reverse()
print(labtops)

# manaf
print("manaf ex sort ")
my_list = [1, 2, 3, 4, 3, 5]
my_list.remove(3)
print(my_list)

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)


## abdfattah

##remove
##نكتب العنصر المطلوب إزالته
##إن كان العنصر مكرر في القائمة سيتم إزالة أول ظهور للعنصر ضمن القائمة
print("abdfattah ex sort ")
office=["Word","Excel","power point"]
office.remove("Excel")
print(office)

##pop
## نحدد المحرف المطلوب إزالته من القائمة
office1=["Word","Excel","power point"]
office1.pop(1)
print(office1)

office1=["Word","Excel","power point"]
office1.pop()
print(office1)



## jaber
## تفريغ القائمة
print("jaber ex sort ")
my_list = [1, 2, 3, 4, 5]

print("before clear:", my_list)

my_list.clear()
print("after clear:", my_list)

my_list = [1, 2, 3, 4, 5]
print("before remove:", my_list)

my_list.remove(3)
print("after remove:", my_list)


## ex7
## حذف القائمة
## del

books=["demoq","madani","medicen"]

print("ex7 before del",books)
del books
print("ex7 after del",books)
