## sedra


#ex1:
number1=input("enter number1:")
number2=input("enter number2:")
sume=float(number1)+float(number2)
print(sume)
sub=float(number1)-float(number2)
print(sub)
mul=float(number1)*float(number2)
print(mul)
div=float(number1)/float(number2)
print(div)
mood=float(number1)%float(number2)
print(mood)
expon=float(number1)**float(number2)
print(expon)
ddfloor=float(number1)//float(number2)
print(ddfloor)

## abdfattah
#Ex1
x=5
y=2
k=7
l=9
p=3
total=(x+y*k-l/p)
print(total)

#Ex2
def sume(x, y):
    return x + y
def sub(x, y):
    return x - y
def multi(x, y):
    return x * y
def div(x, y):
        return "Error" if y==0 else x/y

print(sume(16,2))
print(sub(16,2))
print(multi(16,2))
print(div(16,2))
print(div(16,0))


##ismail
no=float(input("Enter the first number :"))
ab=input("Enter the operator :")
no2=float(input("Enter the second number :"))
if ab=='+':
    print(no+no2)
elif ab=='-':
     print(no-no2)
elif ab=='*':
     print(no*no2)
elif ab=='/':
     print(no/no2)
elif ab=='**':
     print(no**no2)
elif ab=='//':
     print(no//no2)

## gaith
def calculator():
    print("Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("ندخل هونرفم: "))
    num2 = float(input("ندخل هون رقم: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Invalid input")

calculator()

## manaf
def add(x, y):
    return x + y

# دالة الطرح
def subtract(x, y):
    return x - y

# دالة الضرب
def multiply(x, y):
    return x * y

# دالة القسمة
def divide(x, y):
    if y == 0:
        return "لا يمكن القسمة على الصفر!"
    else:
        return x / y

## maan
def sume(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "لا يمكن القسمة على صفر"
    else:
        return x / y

print("Select operation:")
print("1. sume")
print("2. Sub")
print("3. Mul")
print("4. Div")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", sume(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", sub(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", mul(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", div(num1, num2))

else:
    print("Invalid input")
    