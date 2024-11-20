#Allow the user to input the search term instead of using a predefined value.
#Implement the search functionality based on user input.


# Initializing the name list
name_list2 = ["jake","zac","ion","ron","sam","dave"] 

# Asking the user to enter the name
search_name = input("Which name do you want to search for? ")

# Using an if-else statement to check if the name is in the list
if search_name in name_list2:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")


