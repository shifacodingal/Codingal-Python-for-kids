name = "Penguin"
age = 15
is_student = True
weight = 45.5

print("Name : ", name, "Type of name : ", type(name))
print("Age : ", age, "Type of age : ", type(age))
print("Is Student : ", is_student, "Type of is_student : ", type(is_student))
print("Weight : ", weight, "Type of weight : ", type(weight))
# Typecasting
print("After Type Casting")
age = str(age)
print("Age : ", age, "Type of age : ", type(age))
weight = int(weight)
print("Weight : ", weight, "Type of weight : ", type(weight))
is_student = int(is_student)
print("Is Student : ", is_student, "Type of is_student : ", type(is_student))