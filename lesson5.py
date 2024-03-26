# الجلسة الخامسة في البايثون

# 
x=5
d=int(5)
print(x,d)
# ex فائدة 
g=int(5.1)
print(g)
g2=int(5.99)
print(g2)
#g3=int("5.1")
#print(g3)
#g4=int('5.1')
#print(g4)
g5=int('5')
print(g5)



# floats
g6 =float("5.8")
print(g6)

g7 =float('5.8')
print(g7)

g8 =float("5")
print(g8)

g9 =float(21)
print(g9)

# السلاسل stings
v=str(2)
print (v)
v2=str(3.2)
print(v2)
print(type(v2))
v3=str("2.2")
print(v3)
print(type(v3))
# complex 
b1=1j
b2=complex(1+2j)
b3=-6j

import random
print(random.randrange(1,5))


## strings السلاسل

print("hello")
print('hello')
print("""hello""")

## 
h="Helloh"
print(h)

h2="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(h2)

# array with string

abd="Hello, world!"
print(abd[1])
# طباعة الكلمة student  محرف محرف من السلسة المعطاة
ismail="good student"
print()

#print(ismail[5,6,7,8,9,10,11])
#print(ismail[5,12])
#print(ismail[6,7,8,9,10,11,12])
print(ismail[5:12])
print(ismail[5],ismail[6],ismail[7],ismail[8],ismail[9],ismail[10],ismail[11])
print(ismail[5]+ismail[6],ismail[7],ismail[8],ismail[9],ismail[10],ismail[11])
## طول السلسلة
print(len(ismail))







