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
        try:
            patient_name = str(input("Enter patient full name (Firstname Lastname): "))
            patient_age = int(input('Enter patient age: '))
        except:
            print("\nEnter Proper details")
            return None

        patient_details = patient_queue.search(patient_name, patient_age)
        
        if patient_details == {}:
            print('No patient in queue')
            return

        return patient_details

    def show_calendar(self, patient_queue: PatientLinkedListQueue):
        # temporary show calendar
        patient_queue.display_queue()

    def add_by_files(self, patient_queue: PatientLinkedListQueue):
        Helpers.clear_console()
        print('Add patients by file')
        print("\nDrop your additional CSV file in the Import folder. \nNote: The folder contains default patient data already.")    
        confirm = Helpers.validate_yes_or_no_input("\nProcess the current folder? Y/N: ")
        if confirm:
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
        
            patient_queue.display_queue()

            return patient_queue               
         

    def add_indivdual(self, patient_queue: PatientLinkedListQueue):
        Helpers.clear_console()
        print('Manually add a patient\n')
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
            transefrable=new_patient_json['transferable_contact'])

        return patient_queue
    
    def peek_next_patient(self, patient_queue):
        Helpers.clear_console()
        """Show the next patient without removing them"""
        patient_queue.peek()

    def complete_consultation(self, patient_queue):
        Helpers.clear_console()
        """Remove patient after consultation (POP operation)"""        
        if patient_queue.head is None:
            print("No patients in queue")
            return
        
        print("\nCompleting consultation for:")
        patient_queue.get_head()
        
        # Confirm before removing
        confirm = Helpers.validate_yes_or_no_input("\nRemove this patient from queue? Y/N: ")
        if confirm:
            patient_queue.dequeue(1)
            patient_queue.write_queue_to_file()  # Save changes
            print("✓ Patient removed from queue")
    