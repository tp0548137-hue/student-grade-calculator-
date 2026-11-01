
print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\n----- Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")
