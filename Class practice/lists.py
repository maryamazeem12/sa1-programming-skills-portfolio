# Homogeneous List / Python Supports  Hetrogeneous List other than C , Java 
names =["Maryam" , "Bathspa" , "Code Lab 1" ]
print(names)



#  Hetrogeneous List 
Student =["Maryam azeem" , " 297" , "8.65"]
print(Student)



# Repitition Operator * To repeat data
numbers = [1,2,3,4]
new_numbers = numbers * 4
print(new_numbers)



# Positive Indexing  
numbers =[5,6,7,8,3,4]
print(numbers[5]) 



# Negative indexing starts from -1  , bcz 0 is a non-negative integer 
numbers =[5,6,7,6,3,4]
print(numbers[-4])



# lens function tells us number of items in the list 
numbers =[5,6,7,8,3,4,3,9,2,78,101,78,5,3,9,23,87]
print("number of elements in a list :" ,len(numbers)) 



# Mutability (Changable) we can change values in the list 
numbers =[5,6,7,8,3,4,78,3,34,12,98,10,32,71,43,90]
(numbers[5])=89
print(numbers)



#Concatenation Dont use small l (list) to write variable name eg (list )
List_1 =[8,1,96,56,0]
List_2=[2,65,87,23,45]

List_3=List_1 + List_2
print (List_3)



# List slicing  - to use one part of list 
new_list =[2,4,6,9,57,90,23,67,59,12,34,12,78,92]
result= new_list [1:8] # 2nd index exclusive index - 1-8 index , total 7 elements  
print(result)



# find elements in list  -if operator 
new_list1 =[1,2,3,5,6,7,8,9]
if 12 in new_list1:
     print("found")
else:
      print ("Not found")



# (not in)  operator 
new_list2 =[11,12,13,14,15,16,17,18,19]
if 20 not in new_list2:
     print("yes")
else:
      print ("No")



# built in methods - append
New_list3 = [4,5,6,6,7]
New_list3.append(8)
print (New_list3) 



#   built in methods - index
New_list4 = [4,5,6,6,7,2,4,5,8,9,1,5]
print (New_list3.index(6))  # Identify index of number 6



#   built in methods - sort
New_list5 = [5,2,1,8,4,10,3]
New_list5.sort()
print(New_list5)  



#   built in methods - reverse
New_list6 = [21,22,23,24,25,26]
New_list6.reverse()
print(New_list6)



#   built in methods - remove
New_list7 = [4,7,6,3,1]
New_list7.remove(1)
print(New_list7)



# min max number
New_list8 = [91,92,100,88,65,77]
print (max(New_list8))
print (min (New_list8))


