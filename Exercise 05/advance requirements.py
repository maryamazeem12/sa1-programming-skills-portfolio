#Advanced Requirement:Leap Year Adjustment: Modify the program to account for leap years. ForFebruary, ask the user if the year is a leap year and adjust the number of daysaccordingly.


# Dictionary of number of days in each month.
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


# ask user to enter the month number
month = int(input("Enter the month number between (1-12): "))

# ask user to enter the year number
year = int(input("Enter the year number: "))

#the month number should be in between 1-12
if 1 <= month <= 12:

#If february is in leap year it will have 29 days,if february is in non-leap year it will have 28 days.
    if month == 2:
        if (year % 400 == 0) :   #leapyear =29days #non-leapyear = 28 days
            print(f"February has 29 days in {year}")
        else:
            print(f"February has 28 days in {year}")
    else:
        print(f"{days_in_month[month]} days in month {month} of {year}")
else:
    print("Invalid month! please enter a month number between 1 and 12.")


