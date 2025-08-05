student = {
    "name": "Alice Smith",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["Python", "Java", "Calculus"]
}

# Accessing values by key เข้าถึงเพื่ออ่านหรือเขียนก็ได้
print(f"Name: {student['name']}")           # Alice Smith
print(f"Age: {student['age']}")             # 20

# Using get() method (safer) เข้าถึงเพื่ออ่าน (ปลอดภัยกว่า)
print(f"Major: {student.get('major')}")     # Computer Science
print(f"Phone: {student.get('phone')}")     # None (key doesn't exist)
print(f"Phone: {student.get('phone', 'Not provided')}")  # Default value ถ้าphonไม่อยู่ในdictแสดงข้อความNot provided

# Accessing nested data ("courses": ["Python", "Java", "Calculus"])
print(f"First course: {student['courses'][0]}")  # Python

# Check if key exists
if 'gpa' in student:
    print(f"GPA: {student['gpa']}")

# Get all keys(ไปหยิบkeyทั้งหมดในdict), values(ไปหยิบvaluesทั้งหมดในdict), and items(ไปหยิบชุดข้อมูลทั้งหมดในdict)
print(f"Keys: {list(student.keys())}")#list(student.keys()
print(f"Values: {list(student.values())}")#list(student.values()
print(f"Items: {list(student.items())}")#list(student.ชุดข้อมูล()


""" modify dictionary """


# Creating a dictionary
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

print(f"Original inventory: {inventory}")

# Adding new items
inventory["grapes"] = 40
inventory["strawberries"] = 15
print(f"After adding items: {inventory}")

# Updating existing items
inventory["apples"] = 45  # Reduce apple count
inventory["bananas"] += 20  # Add more bananas
print(f"After updates: {inventory}")

# Using update() method
new_items = {"mangoes": 35, "pineapples": 10} #ถ้าเป็นข้อมูลที่มีอยู่แล้วก็จะแก้ไขข้อมูลใหม่
inventory.update(new_items)
print(f"After bulk update: {inventory}")

# Update with another syntax
inventory.update(apples=60, bananas=55)
print(f"After keyword update: {inventory}")

# Removing items หาkeyให้เจอถ้ามีดีดออก แล้วเอาสิ่งที่ดีดออกใส่ในremoved_item
removed_item = inventory.pop("strawberries")  # Remove and return value
print(f"Removed {removed_item} strawberries")

del inventory["pineapples"]  # Remove without returning ดีดออกไปเฉยๆแบบไม่ต้องเอาไปเก็บไว้ที่ไหน(ไม่ได้เอาข้อมูลท่ดีดออกไปทำงานต่อ)
print(f"After deletions: {inventory}")

# Remove last item (Python 3.7+) ดีดตัวล่างสุดไว้ในlast_item
last_item = inventory.popitem()
print(f"Last item removed: {last_item}")

# Clear all items
backup = inventory.copy()#ทำสำเนาinventory
inventory.clear()
print(f"After clear: {inventory}")
print(f"Backup: {backup}")