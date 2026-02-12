from Controllers.SchedulingController import SchedulingController
from Helpers.Helpers import Helpers
from constants import CSV_FOLDER_PATH, QUEUE_PATH
from Queue.PatientLinkedListQueue import PatientLinkedListQueue
from Login.Login import Login
from Registration.Registration import Registration
import os

class Application(SchedulingController):
    def __init__(self):
        super().__init__() 

  
    def start_application(self, user_role):
        # initialize queue
        patient_queue = PatientLinkedListQueue()

        # add items from previously added queue         
        if os.path.exists(QUEUE_PATH): # Check first if there is a file 
            patient_queue.add_queue_from_file(QUEUE_PATH)

        if user_role == 1:
            self.admin_menu(patient_queue)
        elif user_role == 2:
            self.doctor_menu(patient_queue)
        elif user_role == 3:
            self.patient_menu(patient_queue)

    def admin_menu(self, patient_queue: PatientLinkedListQueue):
        while True:
            print("\n" + "=" * 50)
            print("Medical Caravan - ADMIN Panel\n")
            
            print("1. Add patients by file")
            print("2. Add individual patient")
            print("3. Search patient in queue")
            print("0. Exit")
            print("=" * 50)
            
            choice = Helpers.validate_menu_choice(0, 3)
            
            if choice == 0:
                break

            elif choice == 1:
                if Helpers.is_folder_empty(CSV_FOLDER_PATH):
                    print("WARNING: Import folder empty. Please add CSV files to continue.")
                else:
                    self.add_by_files(patient_queue)
                    clarify_choice = Helpers.validate_yes_or_no_input("\nDo you want to save the patient to the system?  Y/N: \n")
                    if clarify_choice:
                        patient_queue.write_queue_to_file()    

            elif choice == 2:
                self.add_indivdual(patient_queue)
                clarify_choice = Helpers.validate_yes_or_no_input("\nDo you want to save the patient to the system?  Y/N: \n")
                if clarify_choice:
                    patient_queue.write_queue_to_file() 

            elif choice == 3:
                self.check_my_position(patient_queue)

    def doctor_menu(self, patient_queue: PatientLinkedListQueue):
        while True:
            print("\n" + "=" * 50)
            print("Medical Caravan - DOCTOR Panel\n")

            print("1. Peek next patient")
            print("2. Complete consultation (remove patient)")
            print("0. Exit")
            print("=" * 50)
            
            choice = Helpers.validate_menu_choice(0, 2)
            
            if choice == 0:
                break
            elif choice == 1:
                self.peek_next_patient(patient_queue) # peek
            elif choice == 2:
                self.complete_consultation(patient_queue) # ability to pop

    def patient_menu(self, patient_queue: PatientLinkedListQueue):
        while True:
            print("\n" + "=" * 50)
            print("Medical Caravan - PATIENT Panel\n")

            print("1. Check my position in queue")
            print("0. Exit")
            print("=" * 50)
            
            choice = Helpers.validate_menu_choice(0, 1)
            
            if choice == 0:
                break
            elif choice == 1:
                self.check_my_position(patient_queue)

            if Helpers.validate_yes_or_no_input("\nSearch another patient? Y/N: "):
                Helpers.clear_console()
                continue
            else:
                break

    def check_my_position(self, patient_queue: PatientLinkedListQueue):
        patient_details = self.search_patient(patient_queue)
        
        if patient_details != None:
            patient_postion = patient_queue.get_position(patient_details['name'], patient_details['age'])
        
            print(f"Patient position is: {patient_postion}\n")
            return
        
        print("\nPatient detail error")



      
if __name__ == "__main__":
    #### User Login and Start Screen
    Login.show_start_screen()
    is_new_user = "Are you a new user Y / N?: "
    
    if Helpers.validate_yes_or_no_input(is_new_user):
        Registration.register_new_user()

    is_user_logged_in = Login.login_user()

    if is_user_logged_in:
        application = Application()
        Helpers.clear_console()
        print("Type your role (1. admin, 2. doctor, 3. patient): ")      
        user_role = Helpers.validate_menu_choice(1, 3)

        application.start_application(user_role)

    print("End of Application")
