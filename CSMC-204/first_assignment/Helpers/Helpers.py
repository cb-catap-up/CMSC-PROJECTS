
class Helpers:

    def clear_console():
        print("\033c", end='')


    def validate_yes_or_no_input(input_question):
    
        while True:
            
            # type cast user input to string
            user_input = str(input(input_question))
            
            # returns true if y
            if user_input.lower() == 'y':
                return  True
            # returns false if no
            if user_input.lower() == 'n':
                return  False
            # if invalid input ask user till a valid input is entered
            if user_input.lower() != 'n' or user_input.lower() != 'y':
                print("\nInvalid input. Please enter a valid one.")
                continue
    
    def convert_true_or_false_string_to_boolean(text: str):
        if text.lower() == 'false':

            return False
    
        if text.lower() == 'true':

            return True

        return None