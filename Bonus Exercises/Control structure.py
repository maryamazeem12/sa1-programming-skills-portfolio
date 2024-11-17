#Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

   #VERSION 1
#assigning a variable to the alein color
alien_color = "red"

#using if statement to test the color of the alien is red
if alien_color.lower () == "red" :
    
 #If the color of the alien is red print the message
    print("Wow, you have just earned 5 points")


    #VERSION 2
#assigning a variable to the alein size
alein_size = "large"

#using if statement to test the size of the alein is large
if alein_size.lower () == "large" :

 #If the size of the alein is large print the messae
    print("WOW,you have just earned 5 points")



#NO OUTPUT
#assigning a variable to the alein size
alein_size = "small"    #This will fail the if test and will have no output because the alein size is large

#using if statement to test the size of the alein
if alein_size.lower () == "large" :
    print("ALEINS HAVE LARGE SIZE")  #NO OUTPUT


