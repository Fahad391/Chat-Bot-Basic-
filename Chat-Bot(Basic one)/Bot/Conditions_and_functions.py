from Dictionary import *
from Abilities.can_math import BasicMath

class Bot:
    @staticmethod # Made it static method for not present it as class or instance method 
    def response():
        while True:
            user = input("Me: ").strip().capitalize() # We can approach it and it responds accordingly
                                                 # Used  Capitalize for converting lower-case input to upperr-case   
            # It'll response the way we approach it
            if user in greetings: 
                print("In response:", greetings[user])
            
            elif user in asking_condition:
                 print("In response:", asking_condition[user])
            elif user in mathematics:
                print("In response:", mathematics[user])
            elif user == 'Do math':
                print("I can do Addition, Subtraction, Multiplication, and Division")
                operation = input("Which one would you like me to perform? ").capitalize()
                
                # Get numbers from the user
                numbers = input("Please enter numbers separated by spaces: ")
                try:
                    # Convert input string into a list of floats
                    nums = list(map(float, numbers.split()))
                    
                    # Instantiate BasicMath with these numbers
                    math_operations = BasicMath(*nums)

                    # Call the appropriate method based on user choice
                    if operation == 'Addition':
                        math_operations.addition()
                    elif operation == 'Subtraction':
                        math_operations.subtraction()
                    elif operation == 'Multiplication':
                        math_operations.multiplication()
                    elif operation == 'Division':
                        math_operations.division()
                    else:
                        print("Sorry, I can only do Addition, Subtraction, Multiplication, and Division.")

                except ValueError:
                    print("Invalid input. Please enter numeric values only.")

            
            else:
                print("Sorry ☹. I'm not able to do that right now")
                print("If I'm upgraded in future I may become able to do so.")

