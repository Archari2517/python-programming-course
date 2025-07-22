# Complete this program to classify people by age
#age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("Enter age: "))
if age >= 60:
    print("Your are Senior")
elif age >= 20:
    print("Your are Adult")
elif age >= 13:
    print("Your are Teenager")
else:
    print("Your are Child")
