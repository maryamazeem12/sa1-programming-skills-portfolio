#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.

#Dictionary of number of days in each month. 
days_in_month = {1: 31,  # January #month1 #31days
    2: 28,  # February     #month2 #28days
    3: 31,  # March        #month3 #31days 
    4: 30,  # April        #month4 #30days
    5: 31,  # May          #month5 #31days
    6: 30,  # June         #month6 #30days
    7: 31,  # July         #month7 #31days
    8: 31,  # August       #month8 #31days
    9: 30,  # September    #month9 #30days
    10: 31, # October      #month10 #31days
    11: 30, # November     #month11 #30days
    12: 31  # December     #month12 #31days
}

#2. Input handling: ask the user for the month number

#providing input to the user asking to enter the month number
month = int(input("Enter the month number between (1-12): "))

#3. Check if the input month number is valid

#Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month. 

# print the number of days in each month if input is valid
if 1 <= month <= 12:
    print(f"Month {month} has {days_in_month[month]} days.")
    #if the input is invalid it will not print the days in month.
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
