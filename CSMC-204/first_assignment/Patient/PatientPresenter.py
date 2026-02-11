from Patient.Patient import Patient

class PatientPresenter(Patient):
    def __init__(self, 
                 patient_id, 
                 name, 
                 age, 
                 sex, 
                 barangay, 
                 serious_condition=False, 
                 comorbidities=False, 
                 disability=False, 
                 transferable_contact=False):

        super().__init__(patient_id, 
                         name, 
                         age, 
                         sex, 
                         barangay, 
                         serious_condition, 
                         comorbidities, 
                         disability, 
                         transferable_contact)
    
    def show_basic_details(self):
        print("───●──────────●─────PATIENT DETAILS─────●──────────●──────────")

        print(f"NAME: {self.patient_id}")
        
        print(f"AGE: {self.age}")

        # print(f"DATE: {self.date}")
        
        print("───●──────────●─────────────────────────●──────────●──────────")

        


    