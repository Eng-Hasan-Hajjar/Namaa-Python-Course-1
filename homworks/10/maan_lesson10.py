# حالات أخرى لتابع splitlines()
#(keepends) اختياري
#ex1
"""
txt="Hello ,\n welcome\n to our course\n"
x=txt.splitlines(keepends=True)
print("ex1",x)
#ex2
txt="Hello ,\n welcome\n to our course\n"
x=txt.splitlines(keepends=False)
print("ex2",x)
"""
#برنامج تحويل الأحرف الصغيرة إلى كبيرة والعكس
text = "Hello welcoMe to our course"
r=text[8:19]
x = ""
for char in r:
    if char.islower():
        x += char.upper()
    if char.isupper():
        x += char.lower()
print(text[:8]+x+text[19:])

