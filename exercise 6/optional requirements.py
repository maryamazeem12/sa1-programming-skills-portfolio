#Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.


#Enter the correct password
correct_password ="iamhere1234" 

#number of attempt limits user has
attempt_limit = 5

#This loop code shows that user will be given the attempt limits to enter the correct password
for i in range (attempt_limit):
    #Prompt asking the user to enter the password
    enter_password = input("enter the correct password:")

 #Check if the password entered by the user is correct
    if enter_password == correct_password:
        print("Congratulations! You're in.")
        break  # Terminate the loop if correct password is entered


    #If the user keep on entering the wrong password inform them about the attempts remaining 
    if i < attempt_limit - 1:
        print(f"wrong password. You have {attempt_limit - i - 1} attempts left.")

else:
    print("Wrong password.Authorities have been alerted!!!!!")




