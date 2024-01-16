Name = input("What is your name? ")

# age = input("Please enter your age: ")
# age = age + 1  # we will run into error as the inputs are recieved in form of strings

age = int(input("Please enter your age: "))
age = age + 1 # we will not run into an error if we use type casting

height = float(input("Please enter your height: "))

print("Hello "+ Name)
print("You will be "+str(age)+" years old in 2025")
print("Rahul is "+str(height)+"cm tall")