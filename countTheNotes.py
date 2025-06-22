Amount = int(input("Please Enter Amount  for Withdrawal : "))

note1 = Amount // 100
note2 = (Amount % 100) // 50
note3 = (Amount % 100 % 50) // 10
print("Number of 100 notes : ", note1)
print("Number of 50 notes : ", note2)
print("Number of 10 notes : ", note3)

