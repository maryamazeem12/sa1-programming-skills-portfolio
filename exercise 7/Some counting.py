#Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case.


# 1. loop that counts up from 0 to 50 in increments of 1.
for i in range(0,51):   #count from 0 to 50
    print(i,end=", " if i != 50 else "\n")  #print the loop in the same line,each number seperated by comma,and no comma after the last number.


print()    #print a blank line to seperate sections to get better output flow


# 2. loop that counts down from 50 to 1 in decrements of 1. 
for i in range(50,-1,-1):  #count from 50 to 0
    print(i,end=", " if i != 0 else "\n")


print()    #to leave a blank space for better structure


# 3. loop that count from 30 to 50.
for i in range(30, 51):  # count from 30 to 50
    print(i,end=", " if i != 50 else "\n")


print()  # to Separate this loop from other loop


# 4. loop that counts from 50 to 10 in decrements of 2.
for i in range (50,9,-2):    # Count from 50 decrease by 2 until reaches 10
   print(i ,end=", " if i != 10 else "\n")


print()  #blank space to seperate loops


# 5. loop that count from 100 to 200 in the increments of 5.
for i in range (100,201,5):   #Count from 100 add 2 until reaches 200
    print(i,end=", " if i != 200 else "\n") #using comma to seperate the number but a newline after 200






