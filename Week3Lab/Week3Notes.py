a=10
#Reassign the variable
a=12
b=12
sum=a+b
print(f"The sum of the 2 variables is {sum}")


#Whats the difference between INT and FLOAT?
#INT: Whole numbers (decimal point, 10,5,3,6
num1=10 #int value, because there's no decimal
#Float: Decimal numbers (10.0,5.0,3.6,6.6)
num2=2.25
word="cat"
print(num1,type(num1))
print(num2,type(num2))
print(word,type(word))
      

#Between these two operators, / and //, which gives INT value and which gives float
#// is floor division and gives INT result
print(10//3)
#/ is regular division and gives Float Result
print(10/3)


user_text=input("Type something: ")
print(user_text)
print(type(user_text))
#No matter what the input is, the data type of user input is always string 
# age_text=input("How old are you now? ") #age_text is a string
# age_number=int(age_text) #This converts our string variable value into an INTZ variable
# print(age_number,type(age_number))
# print(f"Next year you will be {age_number+1}")



#String is what goes between "", string holds no numeric value. Text data
a="54"
b="54"
print(a+b)
word="Python"
print(word[0]) #This will index the first character
print(word[1]) #second character
print(word[2]) #third character

#Slicing (Substring) is when we want to show a range of character
word2="Programming"
print(word2[0:4]) #I want to print the 4 first characters
#print(variable_Name[Start:END])
# #Start at said number, and stop right before END
# print(word2[3:8]) 
# print(word[:6])
# print(word2[6:])
# print(word2[10:5])
# phrase="Hello, World!"
# print("")
# print(phrase.upper()) #To uppercase everything use upper() function
# print (phrase.lower()) #To lowercase everything, use.lower() function

#List is an ordered collection of values, stored within a variable using []
numbers=[10,2,3,5]
word=["cat","dog","Hamster"]
mixed=["Snake", 10.25,3]
print(numbers[0:3]) 
print(numbers)
print(numbers[3])

word.append("Gerbil")
print(word)

word.remove("cat")
print(word)


