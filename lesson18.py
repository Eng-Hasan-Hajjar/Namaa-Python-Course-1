
"""
ismail 29
sedra 18
maan 37
jaber 21
manaf 27
Abd fattah  32
hussam 2
obia 14
gith 19
Bhaa 9
lama 3
ahmad  1

"""

## ex1 
## طباعة جميع العناصر الموجودة في القائمة واحدا تلو الآخر:
office=["Word","Excel","power point"]
for x in office:
    print(x)


## ex2
## حلقة من خلال ارقام الفهارس
## يجب استخدام الدوال range() , len()
office=["Word","Excel","power point"]
for i in range(len(office)) :
    print(office[i])

# ex3

print(range(10))
print(len(office))
print(range(len(office)))


## ex4 
## While
## اطبع جميع العناصر باستخدام حلقة 
## while
## لاستعراض جميع ارقام الفهارس
office=["Word","Excel","power point"]
i=0
while i < len(office):
    print(office[i])
    i=i+1

##ex5
## last element in list
office=["Word","Excel","power point"]
print(office[len(office)-1])
print(office[2])

## ex6
## short hand for (for loop)
## for print all elements in list
office=["Word","Excel","power point"]
[print(x) for x in office ]

## list comprehension
##ex7
office=["Word","Excel","power point"]
newlist=[]
for x in office:
    if "o" in x:
        newlist.append(x) 
print(newlist)        

## ex8
## maan short hand 
office = ["word", "excel", "power point"]
newlist = [x for x in office if "o" in x ]
print(newlist)

##ex9
office=["Word","Excel","power point"]
newlist=[]
i=0
while i < len(office):
    if "o" in office[i]:
        newlist.append(office[i]) 
    i=i+1
print("ex9",newlist)  

## ex 10
office = ["word", "excel", "power point"]
newlist = [x for x in office if x != "power point" ]
print(newlist)

## ex11
newlist2 = [x for x in range(10)  ]
print(newlist2)

## ex12
newlist2 = [x for x in range(10) if x<=5 ]
print(newlist2)