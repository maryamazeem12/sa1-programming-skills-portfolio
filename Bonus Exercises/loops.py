#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,Print a message saying you’ll add that topping to their pizza.


#This while loop continues until all the toppings are entered and they enter "quit" to stopthe loop
#using the while loop
while True:
    #ask the user to enter the toppings of pizza
    pizza_topping = input("enter the toppings you like :")

 
#if the user doesnt wants to add more toping and wants to quit,so
    if pizza_topping.lower () == "quit":
        print("you have a good taste,enjoy your pizza")
        break #break the loop if the user wants to quit and does not wants to add more toppings
    else:
        print(f"I will add {pizza_topping} to your pizza")






