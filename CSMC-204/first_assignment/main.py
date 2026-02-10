from Patient.DataInsertion import DataInsertion
from Patient.MultipleCSV import MultipleCSV
from Registration.Registration import Registration
from Login.Login import Login
from Helpers.Helpers import Helpers
from constants import CSV_PATH, CSV_FOLDER_PATH


class Application:

    def startApplication():
        # #### User Login and Start Screen
        Login.showStartScreen()
        
        is_new_user = "Are you a new user Y / N?: "
        
        if Helpers.validateYesOrNoInput(is_new_user):
            Registration.registerNewUser()

        is_user_logged_in = Login.loginUser()

        if is_user_logged_in:

            #### Data insertion via one single file
            test = DataInsertion.load_csv(CSV_PATH)  
            
            
            print('\nSample data')
            print(test[0])
            print('')


            #### Data insertion via multiple file
            test = MultipleCSV.folder_path(folder=CSV_FOLDER_PATH)
            
            
            print('\nSample data')
            print(test[0][0])
            print('')

            #### Data insertion via manual input
            print("--- Enter New Patient Details ---")
            user_input = [
                input("Name: "),
                input("Age: "),
                input("Sex: "),
                input("Barangay: "),
                input("Serious Condition (True/False): "),
                input("Comorbidities (True/False): "),
                input("Disability (True/False): "),
                input("Transferable Contact (True/False): ")
            ]
            current_manual_id = 1
            new_patient_json = DataInsertion.individual_manual_insert(user_input, current_manual_id)
            test.append(new_patient_json)


if __name__ == "__main__":

    Application.startApplication()

    print("End of Application")



# .txt = db


# def startApp():
    
#     login = login()

#     patients = getPatients()

#     queue = sortPatients(patients)

#     add_calendar = showCalendar(doctors=3, queue, total_hours_of_caravan = 7, avg_consultation_time = 0.5, )


# results = [
#     {
#         "name": 'test',
#         "last_name": 'test'
#     },
# ]
