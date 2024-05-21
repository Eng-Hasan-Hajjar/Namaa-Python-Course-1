present_students = ["Manaf", "Ismaeil", "Lama", "Jaber", "Sedra", "Abd alfatah", "Maan", "Gaith"]

    # طباعة أسماء الطلاب الحاضرين
print("أسماء الطلاب الحاضرين:")
for student in present_students:
        print(student)

    # فحص عدد الطلاب
if len(present_students) > 5:
        print("شكراً لحضوركم جميعاً!")
else:
        print("نتمنى الحضور من الجميع")