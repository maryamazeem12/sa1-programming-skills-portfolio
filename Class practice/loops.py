#This loop prints number upto 10
i = 1
while i < 10:
  print(i)
  i += 1  # i =i+1  

marks = 10
while marks <= 15:
    print("Count is:", marks)
    marks += 1 


#This loop will break the number chain and print 1 2 3 instead of 1-6
j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1   # j=j+1  Both are same 


#this loop will print the list
names = ["maryam", "asna", "aneeka"]
for x in names:
  print(x)


# This loop will print the range fucntion
  for x in range(0,25):
      print (x)

for x in range(10):
     print (x)



#This loop will print the range with readibility
for x in range(0,25):
      print (x, end=",")
         
# Normaly step count (1 increment )
for x in range (0,10,2):    # Count +2 
   print(x ,end=",")

# Count +5
for x in range (0,15,5):
      print(x,end=",")




