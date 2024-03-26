## ex l5
w1="Sedra answer to Question"
print(w1[13]+w1[14])
# اكتب برنامج يقوم بتخزين جميع اسماء الطلاب وأيضا عدد النجوم لكل طالب 
# وفي كل جلسة 


## حلقات في السلاسل
for w in "Sedra answer to Question":
    print(w)

for w in w1:
    print(w)
## ex    
w2="Hu"
for w in w2:
    print(1)
print(len(w2))
print(len(w1))    
## ex

f="Abd"
for v in f :
    #print(6,"Hasan")
    print(v)

## التحقق من السلاسل
k="the player runs in the match"
print("runs" in k)
print()
## 
k="the player runs in the match"
print("runs" not in k)
## النجوم
## عبد الفتاح
## معن 
## حسام
## مناف 
## سيدرة

##مثال
k="the player runs in the match"
if "runs" in k :
    print("yes the word ")
if "eat" in k :
    print("yes the word")   
if "eat" not in k :
    print("not the word")  

## تقطيع السلاسل

n="game, over"
print(n[2:5])

# السلسلة من البداية 
n1="game, over"
print(n1[:7])

# السلسلة الى النهاية 
n1="game, over"
print(n1[5:])

## الفهرسة السلبية
""" 
اطبع المحارف من الحرف 
m
 الى الحرف 
 v 
 مستخدما الفهرسة السلبية
"""
n1="game, over"
print(n1[-8:-2])

## عدل البرنامج بحيث يكون البداية من حرف 
# m 
## الى النهاية
n1="game, over"
print(n1[-8:])

## تحويل السلاسل الى احرف كبيرة
n1="game, over"
print(n1.upper())

##  تحويل السلاسل الى احرف صغيرة
n1="game, OVER"
print(n1.lower())
