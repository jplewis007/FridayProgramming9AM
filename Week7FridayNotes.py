#What is a loop?
#Loop repeats code
#Python uses WHILE and FOR loops

#Repeat this loop 3 times
# for number in range (3):
#     #Print Hello each time the loops runs
#     print("Hello")



#     #While LOOPS
#     #A WHILE loop repeats while a condition is true
#     #Create a starting variable
# number=1
# #keep looping while number is less than or equal to 5
# while number<=5: 
#     #print the current value of number
#     print(number)
#     #Add 1 to number after each loop
#     number+=1


# #Make sure something changes inside a WHILE loop. Other wise you may create a infinite loop

# #WHILE loops with user input
# #A while loop is useful when you want to keep asking until a user gives a valid answer

# #Ask user for their age
# age=int(input("Enter your age:"))
# #Keep looping if the age is less than 1 OR greater than 120
# while age <1 or age > 120:  
#     #Tell the user their input was invalid
#     print("Invalid age")
#     #Ask the user to enter their age again
#     age=int(input("Enter your age:"))
#     #This runs after loop finishes 
#     #Loop stops once the condition becomes FALSE
# print("Age is valid")


# #FOR LOOPS 
# #A for loops works through items one a time

# #Create a list containing anything
# games=["Minecraft", "Mario", "Zelda"]
# #Take one item from the games list at a time
# for game in games:
#     #print the current game
#  #   print(i)





# #Using RANGE()
# #Range() is a sequence of nymbers

# #Start at 2 abd stop before 8
#     for number in range:(2,8) #2 is our starting point and we will stop before 8
# #Print the current number
#     print(number)
#     #Remember the ending number in range() is not included


# #Loop through 2-7
# for number in range:(2,8)
#     #multiply the number itself
# square=number*number
#     #print the squared number
# print(square)


# #Looping through strings 
# # A string can be looped through one character at a time
# #Store a stirng value inside a variable
# word="Tanks"
# #Take one character from the string at a time
# for letter in word:
#     #prints the current letter
#     print(letter)


# #Using BREAK
# #Break stops a loop early
# #loop through number 1-10
# for number in range(1,11):
#     #print the current number
#     print(number)
#     #Want to stop the loop when number is equal to 5
#     if number==5:
#         #Stops the loop immediately
#         break 

#     #Nested Loops
# #Nested loop is inside another loop
# #Outer loop that runs through 1,2,3
# for number in range(1,4):
#     #inner loop also runs through 1,2,3
#     for number2 in range(1,4):
#         #print the current value from both loops
#         print(number,number2)


# #CHOOSING THE RIGHT LOOP
# #use a while loop when repetition depends on a condition
# #Keep looping while answer is not yes
# answer=input("Enter yes")
# while answer !="yes":
#     #ask the user again
#     answer=input("Enter yes") 


# #USE a FOR loop when working through items
# #go through each item in the list
# itemList=[]
# for item in itemlist:
#     #print the current item
#     print(item)

#     #USE FOR with range() when working through numbers
#     #Loop through numbers 1-10
#     for number in range(1,11):
# #print the current number 
#  print(number)

# Counts from 1 to 5
for i in range(1, 6):
    print (i)
while True: 
    user_input = input("Enter something (type 'exit' to quit:)")

    if user_input.lower() == 'exit': 
        print("Goodbye")
    break 

print(f"You entered: {user_input}")

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
for i in range(2, 8):
    print(i) 
    nums = [1, 2, 3, 4, 5]
for i in nums:
    print( i * i)
    name = "Jacob"
for char in name: 
    print(char)


for i in range(1,11):
    print(i)
    if i == 5:
        break
    for x in range(1,4):
     for y in range(1,4):
         print(x,y)
         