#Week 10 Notes, Functions
#What is a function?
# A function is a named set of instructions you can run whenever you want
#Functions let us write code once and reuse it when we need it

#Def(define) a function: create a function starting with def
#Call a function: run the function by using its name with parantheses()
#Parameter: Placeholder variable inside the function definition
#Argument: The real value that we pass into the function via the parameter

#Create a function that says "Hello"
def say_hello():
    print("Hello")
    #Call the function
say_hello()


# #def tells Python "Im defining a function"
# #Code inside the function must be indented
# #Nothing runs until you call it


# #Parameters and Arguments
# def greet(name):
#     #name is thr parameter(placeholder)
#     print(f"Hello, {name}")
# name=input("Enter you name: ")
# greet(name)
# greet("Carl")
# #Parameters are like blanks. Arguments fill them in

# #The only time we need parameters is when we are passing information from outside the function, into the function
# def greet():
#     name=input("Enter your name:")
#     print (f"Hello, {name,}")
#     greet()



# #Print vs Return
# #A function that prints:
def hello_print():
    print("hello world")
# #This shows the text to the user
# #But it does not give a value back to the rest of the program

#A function that Returns:
def hello_return():
    return "Hello World"
#This sends a value back to wherever the function was called
# The caller can store it, print it, etc

msg=hello_return()
print(msg)
result=hello_print()
print(result) #This will print none, because hello_print doesn't return a value back to the function


#Print this for the user. Return is for the program



#Function example 
#Calc program

def calc(num1,num2):
    operator=input("What sort of math do you weant to do: +,-,*,/,")
    #Use if/else to decide what to do
    #perform the math
    #Print or Return the result
    if operator=="+":
        return num1+num2

calc(1,3) #Function now has the value of 4
print(calc)
print(calc(1,3)) #Function now has the value of 4


#Fake loop
# A function can call itself, this is called recursion
# A function can behave like a loop if it repeats until a condition is met 
# If a function is calling itself, it must have a stop condition

#A function that prompts user if they want to continue, if user doesnt want to continue "Loop" stops


def play_again():
    answer=input("Again? (y/n): ").lower()
    if answer =="y":
        play_again()#Calls itself again
    else:
        print("Goodbye")
    play_again





    def greet_user(name):
        print(fHello, {name,}! Welcome.")"
        ""
     #   "Example:"

     greet_user("Jacob")

     def function_calc(num1, num2:):
     op = input("Choose an operation you would like to use (+, -, *, /): ")

     if op == "+": 
     print(f"Result: {num1 + num2}") 
     elif op == "-":
     print(f"Result: {num1 - num2}")
     elief op == "*":
     print(f"Result: {num1 * num2}")
     elief op == "/":
     if num2 != 0:
     print(f"Result: {num1 / num2}")
    else: 
    print("Error: Division by zero")

    else:
    print("Invalid operation")

    funtion_calc(10, 5)

    def get_length(argument):
    return len)argument)

        result = get_length("Python")
        print(result)

        def play_again():
            choice = input("Would you like to play again? (y/n) > ").lower()

            if choice == "y":   
            print("Resetting...")
            play_again()
            else:
                print("Thanks for playing! Goodbye.")

            play_again

