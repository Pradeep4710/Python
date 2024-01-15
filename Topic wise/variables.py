# Variable -> A container for any value

# String datatype

firstname = "Rahul" #string need to be put in double quotes
LastName = "Ghora"
Full_Name = firstname + " " + LastName    # Concatination of strings
print("Hello "+Full_Name)



# Int datatype

age = 21 #int do not need to be in double quotes
print(age) 
age += 1
print("Your age is: "+(str(age))) #Type casting to convert age (int) to a string



# Float datatype

height = 225.50
print(height)
print("Your height is: "+(str(height))+"cm")



# Boolean datatype

human = True
print(human)
print("Are you a human? :- " +(str(human))) 



# Multipe assignment : assigning values to multiple variables in a single line of code

name, age, handsome = "Rahul", 21 , True
print(name, age, handsome)
jan = mar = jul = aug = 31
print(jan , mar , jul , aug)