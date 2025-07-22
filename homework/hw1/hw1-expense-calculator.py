#1. เขียน comment อธิบาย code ในจุดที่สำคัญ ๆ และขอให้มี comment ข้อมูลของผู้วเขียนโปรแกรม
"""
Personal Finance Calculator
Student: [Archari Khemthong]
Date: [Today's Date]
Purpose: Calculate monthly budget and savings
"""
#2. ขอข้อมูลจากผู้ใช้ในประเด็นรายได้ (income) และค่าใช้จ่าย (expense) ดังนี้

while True: #วนloopทำงานจนกว่าเงืิ่อนไขจะเป็นเท็จ
    income=float(input("User's monthly income in THB :")) #รายได้ต่อเดือน
    if income < 0: #ตรวจสอบให้ข้อม ูลที่ผู้ใช้กรอกไม ่น้อยกว่า0
        print("Income can't less than 0\n") #ถ้าน้อยกว่า0ให้แสดงข้อความเตือนและรับค่าอีกครั้ง
        continue
    else:
        break #ถ้าไม่น้อยกว่า0ออกจากloop
while True:
    rent=float(input("User's Monthly rent/housing cost in THB :")) #ค่าเช่า
    if rent < 0: 
        print("Monthly rent/housing cost can't less than 0\n") 
        continue
    else:
        break
while True:
    food=int(input("User's Monthly food budget in THB :")) #ค่ากิน
    if food < 0:   
        print("Monthly food budget can't less than 0\n") 
        continue
    else:
        break
while True:
    transportation=float(input("User's Monthly transportation expenses in THB :")) #ค่าเดินทาง
    if transportation < 0: 
        print("Monthly transportation expenses can't less than 0\n") 
        continue
    else:
        break
while True:
    entertainment=int(input("User's Monthly entertainment budget in THB :")) #ค่าพักผ่อน
    if entertainment < 0: 
        print("Monthly entertainment budget can't less than 0\n") 
        continue
    else:
        break

while True:
    emergency_percent=float(input("User's Percentage to save for emergency (e.g., 10.5) :")) #เผื่อสำหรับฉุกเฉิน%
    if emergency_percent < 0: 
        print("Percentage to save for emergency can't less than 0\n") 
        continue
    else:
        break

while True:
    investment_percent=float(input("User's Percentage to invest (e.g., 15.0) :")) #เงินลงทุน%
    if investment_percent < 0: 
        print("Percentage to invest can't less than 0\n") 
        continue
    else:
        break

#3. คำนวณข้อมูลดังนี้

fixed_expenses = rent + transportation#ค่าใช้จ่ายคงที่
variable_expenses = food + entertainment #ค่าใช้จ่ายไม่คงที่
total_expenses = fixed_expenses + variable_expenses #ค่าใช้จ่ายทั้งหมด
remaining_income = income - total_expenses #รายได้คงเหลือ
emergency_amount = income *(emergency_percent/100) #เงินฉุกเฉิน
investment_amount = income *(investment_percent/100) #เงินลงทุน
available_savings = remaining_income - emergency_amount - investment_amount #เงินเหลือสำหรับออม
expense_ratio = (total_expenses/income) * 100 #สัดส่วนค่าใช้จ่ายต่อรายได้

#4. แสดงออกข้อมูลออกทางหน้าจอ

print("\n=== MONTHLY BUDGET REPORT ===\n")
print(f"Income: {income:.2f} THB") #Income
print(f"Fixed Expenses: {fixed_expenses:.2f} THB") #Fixed Expenses
print(f"Variable Expenses: {variable_expenses:.2f} THB") #Variable Expenses
print(f"Total Expenses: {total_expenses:.2f} THB") #Total Expenses
print(f"Remaining: {remaining_income:.2f} THB") #Remaining
print("\n=== SAVINGS BREAKDOWN ===\n")
print(f"Emergency Fund ({emergency_percent}%): {emergency_amount:.2f} THB") #Emergency Fund 
print(f"Investment ({investment_percent}%): {investment_amount:.2f} THB") #Investment (15%)
print(f"Available for Savings: {available_savings:.2f} THB") #Available for Savings
print("\n=== ANALYSIS ===\n")
print(f"Expense Ratio: {expense_ratio:.2f}%") #Expense Ratio