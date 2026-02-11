from Helpers.Helpers import Helpers
from Queue.PatientLinkedListQueue import PatientLinkedListQueue
from Patient.MultipleCSV import MultipleCSV
from constants import CSV_FOLDER_PATH
from Patient.DataInsertion import DataInsertion
from datetime import datetime

class SchedulingController:
    def __init__(self):
        pass

    def search_patient(self, patient_queue: PatientLinkedListQueue):
        Helpers.clear_console()
        patient_name = str(input("Enter patient full name (Firstname Lastname): "))
        patient_age = int(input('Enter patient age: '))

        patient_details = patient_queue.search(patient_name, patient_age)
        
        # need to ouput output of calendar with date
        print(patient_details['patient_id'])

        if Helpers.validate_yes_or_no_input("Search another patient? Y/N: "):
            self.search_patient(patient_queue)


    def show_calendar(self, patient_queue: PatientLinkedListQueue):
        # temporary show calendar
        patient_queue.display_queue()

    def add_by_files(self, patient_queue: PatientLinkedListQueue):
        
        csv_file = MultipleCSV.folder_path(folder=CSV_FOLDER_PATH)
        for item in csv_file:
            for i in item:
                patient_queue.enqueue(
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
        Helpers.delete_all_files_from_folder(CSV_FOLDER_PATH)
        # temporary show calendar
        self.show_calendar()

    def add_indivdual(self, patient_queue: PatientLinkedListQueue):
        Helpers.clear_console()
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
        current_manual_id = f"idv-{datetime.now()}"
        new_patient_json = DataInsertion.individual_manual_insert(user_input, current_manual_id)
        patient_queue.enqueue(
            patient_id=new_patient_json['patient_id'],
            name=new_patient_json['name'],
            age=new_patient_json['age'],
            sex=new_patient_json['sex'],
            barangay=new_patient_json['barangay'],
            serious_condition=new_patient_json['serious_condition'],
            comorbidities=new_patient_json['comorbidities'],
            disability=new_patient_json['disability'],
            transefrable=new_patient_json['transferable_contact'],)
        
        if Helpers.validate_yes_or_no_input("Add another patient? Y/N: "):
            self.search_patient(patient_queue)
        # temporary show calendar
        self.show_calendar()