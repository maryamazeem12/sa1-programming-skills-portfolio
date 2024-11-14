# A dictionary is a object that stores a collection of data which consists of a key and a value

# The format for creating a dictionary : dictionary = {key1: val1, key2:val2}.


# To add and place value in the dictionary

dictionary = {'color' : 'red' , 'fruit' : 'apple' , 'place' : 'UAE'}
print (dictionary['color'])

dictionary = {'color' : 'red' , 'fruit' : 'apple' , 'place' : 'UAE'}
print (dictionary['fruit'])

dictionary = {'color' : 'red' , 'fruit' : 'apple' , 'place' : 'UAE'}
print (dictionary['place'])

dictionary = { 'name': 'maryam', 'age': '18' }
print(dictionary, 'name:', dictionary['name'])


## Returning a dictionary with a single value

dictionary  = { 'Name' : 'maryam' , 'age ' :  '18' , 'birth place ': 'karachi' } 
print(dictionary["Name"],type(dictionary))

#test the dictionary
dictionary  = { 'Name' : 'maryam' , 'age ' :  '18' , 'birth place': 'karachi' } 
print(dictionary["student"]) 


# Pop Method   

dictionary  = { 'Name' : 'maryam' ,
                'dob' :  '22124' , 
                'Fathers name ': 'Azeem khan' } 
print(dictionary.pop("Name"))
print(dictionary.keys())
print(dictionary.values())


# pop items  - Ot delete items from last value dictionary always return element in the from of tuple 

dictionary  = { 'Name' : 'maryam' ,
                'Roll No' :  '2345' , 
                'Fathers name ': 'azeem' } 
print(dictionary.popitem())
print(dictionary.keys())
print(dictionary.values())


