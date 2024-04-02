#أنواع البيانات في البايثون
#string / int / float / complex / list / tuple / range / dictionary
#set / frozenset / bool / bytes / memoryview / notype
## ضبط نوع البيانات 
## Homework


x=str("Do it today , not tomorrow")
print(x)
print(type(x))               #>>>    <class 'str'>

x=int(2024)
print(x)
print(type(x))               #>>>    <class 'int'>

x=float(30.91)
y=int(34)
print(x,y)
print(type(x),type(y))       #>>>    <class 'float'> <class 'int'>
print(type(x),(y))           #>>>    <class 'float'> 22

C1=complex(8j)                         
print(C1)
print(type(C1))               #>>>    <class 'complex'>

C2=complex(5+25j)
print(C2)
print(type(C2))               #>>>    <class 'complex'>

C3=complex(-5+35j)
print(C3)
print(type(C3))               #>>>    <class 'complex'>

f=float(-48.72)
print(f)
print(type(f))               #>>>    <class 'float'>  لا يحتوي على رقم وهمي و إنما رقم عشري

Li=list(["Assessment","Exercise","Follow up"]) # ((( [[[[[[[ " " ]]]]]]] )))
print(Li)                     #>>>    ['Assessment', 'Exercise', 'Follow up']
print(type(Li))               #>>>    <class 'list'>

Tu=tuple(("Assessment","Exercise","Follow up"))    # ((   ((((((( " " )))))))   ))
print(Tu)                     #>>>    ('Assessment', 'Exercise', 'Follow up')
print(type(Tu))               #>>>    <class 'tuple'>

Se=set({"Assessment","Exercise","Follow up"}) # (((   {{{{{{{ " " }}}}}}}   )))
print(Se)                     #>>>    {'Exercise', 'Follow up', 'Assessment'}
print(type(Se))               #>>>    <class 'set'>

FrozSe=frozenset({"Assessment","Exercise","Follow up"}) # frozenset(  {{{{{{{ "  " }}}}}}}  )
print(FrozSe)                     #>>>    frozenset({'Exercise', 'Follow up', 'Assessment'})
print(type(FrozSe))               #>>>    <class 'frozenset'>

Dic1=dict({"Code":"YAD-82","Quantity":15})
print(Dic1)                        #>>>    {'Code': 'YAD-82', 'Quantity': 15}
print(type(Dic1))                  #>>>    <class 'dict'>

R=range(12)
print(R)                      #>>>    range(0, 12)
print(type(R))                #>>>    <class 'range'>

Boo=bool(True)                       #اذا كتبت الحرف الأول صغير سيعطينا خطأ و يعتبرها قيمة غير منطقية
print(Boo)                     #>>>    True
print(type(Boo))               #>>>    <class 'bool'>

Boo2=bool(False)                      #اذا كتبت الحرف الأول صغير سيعطينا خطأ و يعتبرها قيمة غير منطقية
print(Boo2)                     #>>>    False
print(type(Boo2))               #>>>    <class 'bool'>

By=b"Physical activity"
print(By)                       #>>>    b'Physical activity'
print(type(By))                 #>>>    <class 'bytes'>

ByArr=bytearray(2)
print(ByArr)                    #>>>    bytearray(b'\x00\x00')
print(type(ByArr))              #>>>    <class 'bytearray'>

ByArr5=bytearray(5)
print(ByArr5)                   #>>>    bytearray(b'\x00\x00\x00\x00\x00')
print(type(ByArr5))             #>>>    <class 'bytearray'>
