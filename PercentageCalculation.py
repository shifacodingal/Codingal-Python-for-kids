print("Enter Marks obtained in 5 subjects out of 100 each:")
Math = int(input("Maths: ") )
English = int(input("English: "))
Science = int(input("Science: "))
Social = int(input("Social: "))
Hindi = int(input("Hindi: "))
Total = Math + English + Science + Social + Hindi
Percentage = (Total / 500) * 100
print("Total Marks: ", Total)
print("Percentage: ", Percentage)