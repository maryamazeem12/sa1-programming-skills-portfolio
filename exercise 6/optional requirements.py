#Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If themaximum number of attempts is reached, inform the user that the authoritieshave been alerted.

#Enter the correct password
correct_password = "12345"

#Maximum number of attempts to enter the correct password
attempt_limit = 5

#Give user 5 chances to enter the corect password
for i in range (attempt_limit):  #5
    #the user will enter the password
    entered_password = input("enter the correct password")

    #check if the user enter the correct password
    if entered_password == correct_password:
        print("congratulations!you'r in.")
        break     #terminate the loop because correct password is entered

#let the user know the attemp limits
else:
    print(f"Incorrect password. {attempt_limit - i - 1} tries are left.")
    
#if the attempts limit is finish let the user know that authorities have been alerted.
    if entered_password != correct_password:
        print("All attempts are used. The authorities have been alerted.")
        
        
        

    


     
