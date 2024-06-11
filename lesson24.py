"""
maan 59
Abd fattah  55
ismail 36
manaf 39
gith 32
sedra 34
jaber 21
obia 16
Bhaa 9
lama 3
hussam 2
ahmad  1

"""
"""
from tkinter import *
## التابع الباني
pro= Tk()
## عنوان مربع الواجهة
pro.title("Feedback Tracker")
## أبعاد مربع الواجهة
pro.wm_geometry("900x600+200+50")
## منع التغيير لحجم الواجهة حسب البارامترات
pro.resizable(False,True)
## بقاء الواجهة ظاهرة بشكل مستمر 
pro.mainloop()


import tkinter as tk

# تعريف الدالة التي تغلق التطبيق
def close_app():
    root.destroy()

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Hello World App")
root.geometry("300x200")

# إنشاء علامة نصية مكتوب عليها "Hello World"
label = tk.Label(root, text="Hello World", font=("Arial", 20))
label.pack(pady=20)

# إنشاء زر الخروج
exit_button = tk.Button(root, text="خروج", command=close_app, font=("Arial", 14))
exit_button.pack(pady=1)

# تشغيل حلقة التطبيق الرئيسية
root.mainloop()

"""
"""
from tkinter import *

pro = Tk()
pro.title("ghaith")
pro.wm_geometry("800x400+200+50")
pro.resizable(True, True)
calculator_frame = Frame(pro)
calculator_frame.pack(pady=20)

calc_display = Entry(calculator_frame, width=40, borderwidth=5, font=("Arial", 18))
calc_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#
def button_click(number):
    current = calc_display.get()
    calc_display.delete(0, END)
    calc_display.insert(0, current + str(number))

def button_clear():
    calc_display.delete(0, END)

def button_equal():
    try:
        result = str(eval(calc_display.get()))
        calc_display.delete(0, END)
        calc_display.insert(0, result)
    except:
        calc_display.delete(0, END)
        calc_display.insert(0, "Error")

# تعريف الأزرار
button_1 = Button(calculator_frame, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(calculator_frame, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(calculator_frame, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(calculator_frame, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(calculator_frame, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(calculator_frame, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(calculator_frame, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(calculator_frame, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(calculator_frame, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = Button(calculator_frame, text="0", padx=20, pady=20, command=lambda: button_click(0))

button_add = Button(calculator_frame, text="+", padx=20, pady=20, command=lambda: button_click("+"))
button_subtract = Button(calculator_frame, text="-", padx=20, pady=20, command=lambda: button_click("-"))
button_multiply = Button(calculator_frame, text="", padx=20, pady=20, command=lambda: button_click(""))
button_divide = Button(calculator_frame, text="/", padx=20, pady=20, command=lambda: button_click("/"))

button_equal = Button(calculator_frame, text="=", padx=50, pady=20, command=button_equal)
button_clear = Button(calculator_frame, text="Clear", padx=40, pady=20, command=button_clear)

# وضع الأزرار في الشبكة
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=4)

# بدء الحلقة الرئيسية للتطبيق
pro.mainloop()
"""
"""
from tkinter import *
import webbrowser

def myfunction():
    link=mytext.get()
    webbrowser.open(link)
       
myframe=Tk()
myframe.title("My App")

mylabel=Label(myframe, text="web browser", font="tahome 30 bold")
mylabel.pack(pady=30)

mytext=Entry(myframe, width=50)
mytext.pack(pady=10)

mybutton=Button(myframe,text="Go to link", fg="blue",bg="yellow", font="helvatica 20 bold",padx=10 , pady=3, command=myfunction)
mybutton.pack()

myframe.mainloop()
"""

## if
##ex1
a=100
b=200
if a>b:
    print("ex1","a>b")


## if...  else...
##ex2
a=100
b=200
if a>b:
    print("ex2","a>b")
else:
    print("ex2","a<b")



## if... elif ...  else...
##ex3
a=100
b=200
if a>b:
    print("ex3","a>b")
elif a==b:
    print("ex3","a=b") 
else:
    print("ex3","a<b")       


  ## short hand  
## if
##ex4
a=100
b=200
if a>b: print("ex4","a>b")


  ## short hand  
## if .. else
##ex5
a=100
b=200
print("ex5","a>b")  if a>b else print("ex5","a<=b")


  ## short hand  
## if .. else elseif
##ex6
a=100
b=200
print("ex6","a>b")  if a>b else print("ex6","a=b") if a==b else print("ex6","a>b")


  
## if .. with and
##ex7
a=100
b=20
c=300
if a>b and c>a:
    print("ex7","both of conditions are true")

## if .. with or
##ex8
a=100
b=20
c=300
if a>b or c>a:
    print("ex8","at least one of conditions is true")    

## if .. with not
##ex9
a=100
b=20

if not a<b :
    print("ex9","a is not smaller than b")    

## if ..nested
##ex10
x=55
if x>20:
    print("ex10","x>20")
    if x> 30:
       print("ex10","x>30")
    else: 
       print("ex10","x<30")      


## if ..pass
##ex11
x=55
if x>20:
    pass 

##homework

x = 10

if x > 5:
    pass  
else:
    print("x is 5 or less")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number % 2 == 0: 
        pass  
    else:
        print(number)

x = 10  # تحديد قيمة المتغير x

if x > 5:
    print("x is greater than 5")  # طباعة رسالة إذا كانت قيمة x أكبر من 5
else:
    print("x is 5 or less")  # طباعة رسالة إذا كانت قيمة x تساوي 5 أو أقل


a = 33
b = 200
c = 150

if a > b:
    print("a is greater than b")
    if c > b:
     print("c is greater than b")
     if a == b:
      pass  
else:
    print("a and b are not equal")

x = 10
if x > 5:
    pass 
else:
    print("x is 5 or less")


## dict nested المتداخلة 
##ex12

myfamily={
    "child1":{
        "name":"jamil",
        "year":"2006"
    },
     "child2":{
        "name":"ahmad",
        "year":"2008"
    },
     "child3":{
        "name":"adnan",
        "year":"2009"
    }
}

##ex13
child1={
        "name":"jamil",
        "year":"2006"
    }
child2={
        "name":"jamil",
        "year":"2006"
    }
child3={
        "name":"jamil",
        "year":"2006"
    } 
myfamily={
      "child1":child1,
      "child2":child2,
      "child3":child3
}



##ex14
child1={
        "name":"jamil",
        "year":"2006"
    }
child2={
        "name":"jamil2",
        "year":"2006"
    }
child3={
        "name":"jamil3",
        "year":"2006"
    } 
myfamily={
      "child1":child1,
      "child2":child2,
      "child3":child3
}


print("ex14",myfamily["child2"]["name"])


## while
## for
#ex15
i=1
while(i<6):
    print("ex15",i)
    i+=1

## while .. break
## for
#ex16
i=1
while(i<6):
    print("ex16",i)
    if (i==3):
        break
    i+=1

## while .. continue
## for
#ex17
i=1
while(i<6):
    i+=1
    if (i==3):
        continue
    print("ex17",i)


## while ..else
## for
#ex18
i=1
while(i<6):
    print("ex18",i)
    i+=1
else:
    print("else with while")


