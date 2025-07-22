# Example: Print only even numbers from 1 to 10 ใช้เมื่อรู้จำนวนรอบ(range ทำหน้าที่ list of data โดยเพิ่มขึ้นทีละ 1)
for i in range(1, 11):#loop วน 10 รอบ (ตั้งแต่ 1 ถึง 11-1 )
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
        
# Example: Input validation ใช้เมื่อไม่่รู้จำนวนรอบ
password = ""#ตัวแปรประเภทstring
while len(password) < 8:#ในระหว่างที่เป็นจริง
    password = input("Enter a password (at least 8 characters): ")
    if len(password) < 8:
        print("Password too short! Try again.")
print("Password accepted!")


# Example: Multiplication table 
for i in range(1, 4):  # rows
    for j in range(1, 4):  # columns
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # new line after each row
    
    
    
# Break example: Find first number divisible by 7
for num in range(1, 100):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break#ออกจากloopที่อยู่ใกล้กับตัวมันมากที่สุด

# Continue example: Skip negative numbers
numbers = [5, -3, 8, -1, 12, -7, 4]
for num in numbers:
    if num < 0:
        continue  # skip negative numbers กระโดดไปหัวloopที่อยู่ใกล้ตัวมันมากที่สุด
    print(f"Positive number: {num}")