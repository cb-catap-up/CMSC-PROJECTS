import os


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
    
    def validate_menu_choice(min_option, max_option):
        """Validate user menu input is within valid range."""
        while True:
            try:
                choice = int(input(f"Select option ({min_option}-{max_option}): "))
                if min_option <= choice <= max_option:
                    return choice
                else:
                    print(f"Invalid choice. Please enter a number between {min_option} and {max_option}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def delete_all_files_from_folder(folder_path):

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

        print("All files deleted successfully.")

    def is_folder_empty(folder_path):

        if os.listdir(folder_path):
            return False
        else:
            return True
