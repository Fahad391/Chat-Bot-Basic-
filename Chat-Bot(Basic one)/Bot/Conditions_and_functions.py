from Dictionary import *
from Abilities.can_math import *

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
                    elif operation == 'Square':
                        # Now it'll handle Mid-level math
                        math_operations = Mid_Level_Math(*nums)
                        math_operations.square()
                    elif operation == 'Cube':
                        math_operations = Mid_Level_Math(*nums)
                        math_operations.cube()

                except ValueError:
                    print("Invalid input. Please enter numeric values only.")
            elif user in time_date:
                print("In Response: ", time_date[user])
            elif user in other_resposnse:
                print("In response: ", other_resposnse[user])
            
            else:
                print("Sorry ☹. I'm not able to do that right now")
                print("If I'm upgraded in future I may become able to do so.")

