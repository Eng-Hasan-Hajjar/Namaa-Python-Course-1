#is , is not:
#هما معاملان لمقارنة قيم المتحولات في الذاكرة
#ex1: is
x=2
y=2
z=3
print("ex1",x is y)
print("ex1",x is z)
#ex2: isnot
x=2
y=2
z=3
print("ex2",x is not z)
print("ex2",x is not y)
# in , not in:
#هما معاملان للتحق من وجود قيمة داخل تسلسل مثل
#list , tuple , set , str
#ex3: in
ls=[1,2,3]
print("ex3",3 in ls)
print("ex3",5 in ls)
#ex4: not in
ls=[1,2,3]
print("ex4",5 not in ls)
print("ex4",3 not in ls)
"""
stu = {"ismail":21,"sedra":13,"maan":25,"jaber":12,"manaf":17,"abd alfattah":21
       ,"hussam":2,"obai":13,"hith":11,"bhaa":9,"lama":1,"ahmad": 1}
while True:
    stu_name = input("Enter student name (or 'exit'):")
    if stu_name.lower() == 'exit':
        break
    stu_mark = int(input("Enter student mark:"))

    if stu_name in stu:
        stu[stu_name] += stu_mark
        print(stu)
    else:
        print("Error in name")
"""
