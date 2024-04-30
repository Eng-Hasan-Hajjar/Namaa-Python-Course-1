#First homework
#Splitlines()
#يقوم بتقسيم سلسلة نصية إلى قائمة من السلاسل
#تقوم هذه الدالة بفصل السلسلة عن طريق الأسطر الجديدة (\n)
#وكذلك السلسلة الفارغة ('')
# التي تظهر في نهاية السلسلة إذا كانت السلسلة الأصلية تنتهي بسطر جديد
#فصل هذه البيانات إلى أجزاء قابلة للمعالجة
#تقسيم النص إلى أسطر لمعالجتها بشكل منفصل

text = "New York, USA \n Paris, France \n London, UK"
x=text.splitlines()
print(x)
# result>>>> ['New York, USA ', ' Paris, France ', ' London, UK']

text1 = """New York, USA  
Paris, France  
London, UK"""
x1=[line.split(', ') for line in text1.splitlines()]
print(x1)
# result>>>> [['New York', 'USA  '], ['Paris', 'France  '], ['London', 'UK']]






#Second homework
# تحويل الأحرف الكبيرة إلى صغيرة و الأحرف الصغيرة إلى كبيرة ضمن مجال معين في النص
txt = "Hello my name is Abbdulfettah"
start_index = 8
end_index = 17
x = txt[:start_index] + txt[start_index:end_index].swapcase() + txt[end_index:]
print(x)



txt = "Hello my name is Abbdulfettah"
x = txt[:8] + txt[8:17].swapcase() + txt[17:]
print(x)

