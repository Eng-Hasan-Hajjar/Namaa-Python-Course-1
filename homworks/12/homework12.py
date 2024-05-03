## maan

def namaa():
    return False
if namaa()==True:
    print("معن")
else :
    print("عبد الفتاح")


## manaf
def students_stars(name):
    if name == "معن":
        return 3
    if name == "عبد الفتاح":
        return 4
    else:
        return None

num=students_stars("معن")
num2=students_stars("عبد الفتاح")
num3=students_stars("")

print(num,num2,num3)

## jaber
def check_value(x):
    if x:
        print("معن")
    else:
        print("عبد الفتاح")


value = True
check_value(value)        

## ismail
x=7>4
def my_function(x):
    if x : return "معن"
    else : return "عبد الفتاح"
print(my_function(x))


## Abd fattah

def my_function(list):
     return "Abdulfettah" if "Abdulfettah" in list else "Maan"
print("Abd fattah 1",my_function(["Abdulfettah","Maan","İsmail","Ahmed"]))

def my_function(list):
     return "Abdulfettah" if "Abdulfetah" in list else "Maan"
print("Abd fattah2",my_function(["Abdulfettah","Maan","İsmail","Ahmed"]))



def my_function(x):
     return "Abdulfettah" if x == 25 else "Maan"
print("Abd fattah3",my_function(25))


def my_function(x):
     return "Abdulfettah" if x == 25 else "Maan"
print("Abd fattah 4",my_function(52))


## sedra


#ex1
def maan_Function():
    return True
print("ex1",maan_Function())
#ex2:
def abd_Function():
    return False 
print("ex2",abd_Function())
if maan_Function ():
    print("maan")
else :
    print("abd")
if abd_Function  () :
     print("maan")
else :
     print("abd")