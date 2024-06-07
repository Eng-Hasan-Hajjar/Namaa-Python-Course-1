"""
maan 53
Abd fattah  49
ismail 34
manaf 38
gith 28
sedra 29
jaber 21
obia 16
Bhaa 9
lama 3
hussam 2
ahmad  1

"""

dictionary1={
    "brand":"BMW", 
    "model":"x5",
    "year":"2016"
}
dictionary2={
    "brand":"rangerover", 
    "model":"d8",
    "year":"2020"
}


##ex1
##print elements from dict

dictionary={
    "brand":"BMW", 
    "model":"x5",
    "year":"2016"
}

print(dictionary)


##ex2
##print element for brand from dict

dictionary={
    "brand":"BMW", 
    "model":"x5",
    "year":"2016"
}

print("ex2 ",dictionary["brand"])

##ex3


dictionary={
    "brand":"BMW", 
    "model":"x5",
    "year":"2015",
    "year":"2016"
}

print("ex3 ",dictionary)

##ex4


dictionary={
    "brand":"BMW", 
    "model":"x5",
    "year":"2015"
}

print("ex4 ",len(dictionary))


##ex5
## data types in dict

dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}

print("ex5 ",dictionary)


## عبد الفتاح 
my_dict = {
    "fruits": ["apple", "banana", "cherry"],
     "letters": {"a", "b", "c"}
}
print(my_dict)


##ex6
## data types in dict

dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}

print("ex6 ",type(dictionary))


##ex7
## data types in dict

dictionary=dict(brand="BMW",model=True,country="Syria",numberdoor=4)


print("ex7 ",type(dictionary),dictionary)


##ex8
## access to elements
dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}
x=dictionary["brand"]
print("ex8 ",type(dictionary),x)


##ex9
## access to elements
dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}
x=dictionary.get("year")
print("ex9 ",type(dictionary),x)



##ex10
## access to elements
dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}
x=dictionary.values()
print("ex10 ",x)



##ex11
dictionary={
    "brand":"BMW", 
    "model":True,
    "year":2015,
    "colors":["red","blue","black"]
}
x=dictionary.values()
print("ex11 ",x)
dictionary["year"]=2020

print("ex11-2 ",x)


##ex12
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
x=dictionary
print("ex12 ",x)



##ex13
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
x=dictionary.items()
print("ex12 ",x)


##ex14
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
if "model" in dictionary:
    print("ex14 ","model exist")

##ex15
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
dictionary.update({"year":2019})

print("ex15 ",dictionary)

##ex16
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
if "price" in dictionary:
    print("ex16 ","price exist")
else :
      dictionary.update({"price":2000})  

print("ex16 ",dictionary)


##ex17
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
if "price" in dictionary:
    print("ex17 ","price exist")
else :
      dictionary["price"]=2500  

print("ex17 ",dictionary)



##ex18
##pop()
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
if "price" in dictionary:
    print("ex18 ","price exist")
else :
      dictionary["price"]=2500  

print("ex18 ",dictionary)
dictionary.pop("price")
print("ex18 ",dictionary)



##ex19
##popitem()
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
if "price" in dictionary:
    print("ex19 ","price exist")
else :
      dictionary["price"]=2500  

print("ex19 ",dictionary)
dictionary.popitem()
print("ex19 ",dictionary)



##ex20
##del
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}


print("ex20 ",dictionary)
del dictionary
#print("ex20 ",dictionary)
##ex21
##
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
if "price" in dictionary:
    print("ex21 ","price exist")
else :
      dictionary["price"]=2500  

print("ex21 ",dictionary)
del dictionary["brand"]
print("ex21 ",dictionary)




##ex22
##
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
if "price" in dictionary:
    print("ex22 ","price exist")
else :
      dictionary["price"]=2500  

print("ex22 ",dictionary)
dictionary.clear()
print("ex22 ",dictionary)

##ex23
## for
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}

for x in dictionary:
    print("ex23 for ",x)


##ex24
## for
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}

for x in dictionary:
    print("ex24 for ",dictionary[x])


##ex25
## for
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}

for x in dictionary.values():
    print("ex25 for ",x)


##ex26
## for
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}

for x in dictionary.items():
    print("ex26 for ",x)



##ex27
## copy
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
dictionary2=dictionary.copy()

print("ex27 for ",dictionary2)



##ex28
## dict copy
dictionary={
    "year":2015,
    "colors":["red","blue","black"],
    "brand":"BMW", 
    "model":True,
   
}
dictionary2=dict(dictionary)

print("ex28 for ",dictionary2)


## homworks


##sedra
#issubset():للتحقق مما ازا كانت المجموعة الفرعية تحتوي على جميع العناصر في المجموعة الرئيسية
#ex1
set1={1,2,3,4,5,6}
set2={1,2,3}
is_subset= set1.issubset(set2)
print("ex1",is_subset)
set3={1,6}
is_subset=set3.issubset(set2)
print("ex1",is_subset)

#issuperset(): للتحقق مما ازا كانت المجموعة الرئيسية تحتوي على جميع العناصر في المجموعة الفرعية
set1={1,2,3,4,5,6}
set2={1,2,3}
is_superset=set1.issuperset(set2)
print(is_subset)
set3={1,6}
is_superset=set1.issuperset(set3)
print(is_superset)
#copy():للانشاء نسخة من المجموعة
original_set={1,2,3,4,5,6}
copied_set={1,2,3}
copied_set=set1.copy()
print("ex1",original_set)
print("ex1",copied_set)

##abd fattah

#add()
#تضيف عنصرًا إلى المجموعة
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  #{1, 2, 3, 4}


#clear()
#يزيل جميع العناصر من المجموعة
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  #set()


#copy()
#يُرجع نسخة من المجموعة
my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  #{1, 2, 3}


#difference()
#يُرجع مجموعة تحتوي على الفرق بين مجموعتين أو أكثر
set1 = {1, 2, 3}
set2 = {2, 3, 4}
diff_set = set1.difference(set2)
print(diff_set)  # {1}


#difference_update()
#يزيل العناصر الموجودة في مجموعة معينة والتي توجد أيضًا في مجموعة أخرى
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)  # {1}


#discard()
#يزيل العنصر المحدد إذا كان موجودًا
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # {1, 3}


#intersection()
# يُرجع مجموعة تحتوي على العناصر المشتركة بين مجموعتين
set1 = {1, 2, 3}
set2 = {2, 3, 4}
inter_set = set1.intersection(set2)
print(inter_set)  # {2, 3}


#intersection_update()
# يحتفظ فقط بالعناصر المشتركة بين المجموعة الحالية ومجموعة (أو مجموعات) أخرى
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # {2, 3}


#isdisjoint()
# يُرجع (True) إذا لم يكن هناك أي عناصر مشتركة بين مجموعتين، 
#وإلا يُرجع (False)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # True


#issubset()
#يُرجع (True) إذا كانت كل عناصر المجموعة الحالية موجودة في مجموعة أخرى
# وإلا يُرجع (False)
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # True


#issuperset()
# يُرجع (true) إذا كانت كل عناصر مجموعة أخرى موجودة في المجموعة الحالية
# و إلا فإنه يرجع (False)
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # True


#pop()
# يزيل ويُرجع عنصرًا عشوائيًا من المجموعة
my_set = {1, 2, 3}
popped_element = my_set.pop()
print(popped_element)     # 1
print(my_set)    # {2, 3}


#remove()
# يزيل العنصر المحدد. إذا لم يكن العنصر موجودًا، يعطي خطأ
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # {1, 3}


#symmetric_difference()
# يُرجع مجموعة تحتوي على العناصر التي توجد في مجموعة واحدة فقط، وليس في كلتيهما
set1 = {1, 2, 3}
set2 = {2, 3, 4}
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # {1, 4}


#symmetric_difference_update()
# يحتفظ فقط بالعناصر التي توجد في مجموعة واحدة فقط، وليس في كلتيهما
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)  # {1, 4}


#union()
# يُرجع مجموعة تحتوي على جميع العناصر من جميع المجموعات المحددة (بدون تكرار)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4}


#update()
# يضيف عناصر من مجموعة (أو مجموعات) أخرى إلى المجموعة الحالية
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.update(set2)
print(set1)  # {1, 2, 3, 4}


##maan


##issuperset()
##يتحقق مما إذا كانت المجموعة الحالية تحتوي على جميع عناصر المجموعة الأخرى
#ex1
set1={1,2,3}
set2={1,2}
print("ex1",set1.issuperset(set2))

##issubset()
##يتحقق مما إذا كانت المجموعة الحالية مجموعة جزئية من المجموعة الأخرى
#ex2
set1={1,2}
set2={1,2,3}
print("ex2",set1.issubset(set2))

##isdisjoint()
##يتحقق مما إذا كانت المجموعتان لا تحتويان على عناصر مشتركة
#ex3
set1={1,2,3}
set2={4,5,6}
print("ex3",set1.isdisjoint(set2))

##copy()
##يستخدم لإنشاء نسخة جديدة ومستقلة من المجموعة الأصلية
#ex4
set3={1,2,3}
set4=set3.copy()
print("ex4",set4)
















