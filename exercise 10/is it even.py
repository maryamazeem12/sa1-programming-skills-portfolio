#Write a program that tests if a value is even or odd. Follow the instructions outlined below:

def main():
#asking user to enter a number
      number = int(input("enter the number:"))
      if number & 1 == 0:  #check if the number is even or odd
 #If its a even number print (Even) 
            print("Its a even number")
      else:
#If its a odd number print (odd)
            print("Its a odd number")

#The main function wil run the program
if __name__ == "__main__":
                 main()
            
