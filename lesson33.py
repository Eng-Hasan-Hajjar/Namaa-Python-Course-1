"""
maan 80
Abd fattah  91
ismail 62
manaf 67
gith 57
sedra 61
jaber 21
obia 16
Bhaa 24
lama 3
hussam 2
ahmad  1

"""



## files
try:
    f=open("text.txt")
    f.close()
except:
    print("there is exception file ")    


## r , a , w , x
## t , b
## files
try:
    f=open("text.txt","rt")
    print(f.read())
    f.close()

except:
    print("there is exception file ")    



try:
    f=open("text.txt","rt")
    print(f.read(5))
    f.close()

except:
    print("there is exception file ")    

try:
    f=open("text.txt","rt")
    print(f.readline())
    f.close()

except:
    print("there is exception file ")    


try:
    f=open("text.txt","rt")
    print(f.readline())
    print(f.readline())
    f.close()

except:
    print("there is exception file ")    




try:
    f=open("text.txt","rt")
    print("12")
    print(f.readline(5))
    print(f.readline(6))
    print(f.readline(6))
    print(f.readline(4))
    print(f.readline(5))
    print(f.readline(6))
    print(f.readline(6))
    print(f.readline(4))
    print(f.readline(6))
    f.close()
   
except:
    print("there is exception file ")    


try:
    f=open("text.txt","rt")
    for x in f:
        print(x)
    f.close()

except:
    print("there is exception file ")    

## a- w

try:
    f=open("text.txt","a")
    print(f.write("\nthis is from append"))
    f.close()

except:
    print("there is exception file ")    

try:
    f=open("text.txt","w")
    print(f.write("\nthis is from append"))
    f.close()

except:
    print("there is exception file ")    




try:
    f=open("text2.txt","x")
    print(f.write("\nthis is from append"))
    f.close()

except:
    print("there is exception file ")    


import os

try:
    os.remove("text3.txt")

except:
    print("there is exception file ")    


## excel

##json

