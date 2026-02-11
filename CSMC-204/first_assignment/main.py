from Controllers.SchedulingController import SchedulingController
from Helpers.Helpers import Helpers
from constants import CSV_FOLDER_PATH, QUEUE_PATH
from Queue.PatientLinkedListQueue import PatientLinkedListQueue
from Login.Login import Login
from Registration.Registration import Registration


class Application(SchedulingController):
    def __init__(self):
        super().__init__() 

    # CLYDE
    # Start screeen w/ description -- 
    # login
    # ask if they want to import, search, and show calendar
    # exit or import or search
    # import, by file or invidividual
    # ask if they want to import, search, and show calendar (i, s, c, exit)

    # CALENDAR //JOM
    # number of doctors, total hrs of caravan, hrs of consultation per patient
    # ['1st day ', '2nd day', '3rd day']
    # ['1st person','1st person','1st person']

    # [{'name': 'clyde', 'age': 27},{'name': 'dex', 'age': 18},{'name': 'clyde', 'age': 27}]

    def start_application(self):

        # initialize queue
        patient_queue = PatientLinkedListQueue()

        # add items from previously added queue
        patient_queue.add_queue_from_file(QUEUE_PATH)
        
        
        search_input = Helpers.validate_yes_or_no_input("Search patient schedule? Y/N: \n")

        if search_input:
            self.search_patient(patient_queue)
            return

        # ask user what to do
        user_input = Helpers.validate_yes_or_no_input("Show patients calendar? Y/N: \n")

        if user_input:
            self.show_calendar(patient_queue)
            return
        
        if not user_input:
            add_patient_by_file = Helpers.validate_yes_or_no_input("Add patients by file? Y/N: \n")
            if add_patient_by_file:
                if Helpers.is_folder_empty(CSV_FOLDER_PATH):
                    print('Import folder empty')
                    return
                self.add_by_files(patient_queue)

            if not add_patient_by_file:
                add_individual_patient = Helpers.validate_yes_or_no_input("Add individual patient? Y/N: \n")
                if add_individual_patient:
                    self.add_indivdual(patient_queue)
                    return



if __name__ == "__main__":
    # #### User Login and Start Screen
    Login.show_start_screen()
    is_new_user = "Are you a new user Y / N?: "
    
    if Helpers.validate_yes_or_no_input(is_new_user):
        Registration.register_new_user()

    is_user_logged_in = Login.login_user()

    if is_user_logged_in:
        application = Application()

        application.start_application()

    print("End of Application")
