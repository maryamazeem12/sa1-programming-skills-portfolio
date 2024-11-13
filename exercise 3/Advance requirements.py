#Have the user input their name, hometown, and age instead of hardcoding thevalues. Try giving both your first and second name when asked for your name.What happens? How can you handle multiple words in Python? Test theprogram by entering a string value for age (e.g., “twenty”). What happens?How can you prevent this issue?

#Asking the user to enter their full name (first and last name )
full_name = input("Enter your full name:")

#Asking the user to enter their hometown 
user_hometown = input("Enter your hometown:")

#Asking the user to enter their age
user_age = input("Enter your age:")


#This code is to check if the user have entered an valid integar
if user_age.isdigit():     #this code checks that age must be in the form of integars
    age = int(user_age)   #this code will convert string to integar

else:
    print("Error: Invalid age input") #print error if age is not integar

    age = None #setting age to none to show that invalid age was enetered


#using the F-string format to print the name,hometown,and age of the user

print(f"Name: {full_name}")   #print the name entered by user
print(f"Hometown: {user_hometown}")  #print the hometown entered by user


#if age is entered as an integar so it will print the age otherwise it will show invalid input(age)

if age is not None :
    print(f"Age: {age}")
else:
    print("Age: Invalid age") 
