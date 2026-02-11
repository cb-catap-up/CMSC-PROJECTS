from Patient.DataInsertion import DataInsertion
from Patient.MultipleCSV import MultipleCSV
from Registration.Registration import Registration
from Login.Login import Login
from Helpers.Helpers import Helpers
from constants import CSV_PATH, CSV_FOLDER_PATH
from Queue.PatientLinkedListQueue import PatientLinkedListQueue


class Application:

    def start_application():

        # #### User Login and Start Screen
        Login.show_start_screen()
        
        is_new_user = "Are you a new user Y / N?: "
        
        if Helpers.validate_yes_or_no_input(is_new_user):
            Registration.register_new_user()

        is_user_logged_in = Login.login_user()
        is_user_logged_in = True
        if is_user_logged_in:
            print("--- SINGLE CSV ---")
            #### Data insertion via one single file
            test = DataInsertion.load_csv(CSV_PATH)  
            queue = PatientLinkedListQueue()
            for item in test:
                # print(item['patient_id'])
                queue.enqueue(
                    patient_id=item['patient_id'],
                    name=item['name'],
                    age=item['age'],
                    sex=item['sex'],
                    barangay=item['barangay'],
                    serious_condition=item['serious_condition'],
                    comorbidities=item['comorbidities'],
                    disability=item['disability'],
                    transefrable=item['transferable_contact'],
                )
            queue.display_queue()

            ## Data insertion via multiple file
            print("--- MULTIPLE CSV ---")
            test = MultipleCSV.folder_path(folder=CSV_FOLDER_PATH)

            multiple_csv_queue = PatientLinkedListQueue()

            for item in test:
                for i in item:
                    multiple_csv_queue.enqueue(
                        patient_id=i['patient_id'],
                        name=i['name'],
                        age=i['age'],
                        sex=i['sex'],
                        barangay=i['barangay'],
                        serious_condition=i['serious_condition'],
                        comorbidities=i['comorbidities'],
                        disability=i['disability'],
                        transefrable=i['transferable_contact'],
                    )
            multiple_csv_queue.display_queue()
            ### Data insertion via manual input
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
            multiple_csv_queue.enqueue(
                        patient_id=new_patient_json['patient_id'],
                        name=new_patient_json['name'],
                        age=new_patient_json['age'],
                        sex=new_patient_json['sex'],
                        barangay=new_patient_json['barangay'],
                        serious_condition=new_patient_json['serious_condition'],
                        comorbidities=new_patient_json['comorbidities'],
                        disability=new_patient_json['disability'],
                        transefrable=new_patient_json['transferable_contact'],
                    )
            multiple_csv_queue.display_queue()


if __name__ == "__main__":

    Application.start_application()

    print("End of Application")
