#IF STATEMENT - ELIF
a = 40
b = 200
if b > a:
    print("a is greater than b")
else: 
    print("b is greater than a")


a = 25
b = 25
if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b")


b = 80
p = 90
if b!=p:
    print("b isn't same as p")
else:
    print("b is same as p")



#Nested decision structures and the if-elif-else statement

salary = int (input("Enter your salary :"))
if salary >= 30000:
    years_on_job = float(input ("Enter the years of job: "))
    if years_on_job >= 2:
        print("You qualify for your job")
    else :
        print ("experience is less than 2")

else:
     print ("you earn atleast 30 k to qualify")



#elif

#using nested decision structure to determine a grade

#taking input from the user
score = int(input("enter your score :"))
#check if the score is greater than 90 your grade is A
if score >=90:
    print("your grade is A.")
#check if the score is greater than 80 your grade is b
elif score >=80:
    print("your grade is B.")
#check if the score is greater than 70 your grade is c
elif score >=70:
    print("your grade is C.")
#check if the score is greater than 60 your grade is d
elif score >=60:
    print("your grade is D.")
#check if the score is less than 60 you r fail
if score <60:
    print("your grade is fail")
