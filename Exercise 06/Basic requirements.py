
# Step 1: Define the correct password

#correct password
correct_password = "25946"

# Step 2: Use a while loop to repeatedly ask the user for the password until the correct one is entered. 

#The while loop will continue to run until the user enter the correct password
while True:
    # Ask to enter the correct password
    enter_password = input("Enter the password: ")
    
 # Step 3: Output an appropriate message when the correct password is entered.

#If the user will enter the correct password so it will print the message
    if enter_password == correct_password:
        print("Password is correct! You'r in.")
        break  #Terminate the loop if the correct password is entered.
    else:
        print("Incorrect password! Try again please.")
    
