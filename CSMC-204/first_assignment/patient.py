class Patient:
    """Represents a patient with health information"""
    def __init__(self, patient_id, name, age, sex, barangay, serious_condition=False, comorbidities=False, disability=False, transferable_contact=False):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.sex = sex
        self.barangay = barangay
        self.serious_condition = serious_condition
        self.comorbidities = comorbidities
        self.disability = disability
        self.transferable_contact = transferable_contact
        
        self.priority_score = 0
        self.scheduled_date = None
        self.scheduled_time = None
        self.queue_position = None

    def __repr__(self): # for display purposes
        return f"Patient(ID: {self.patient_id}, Name: {self.name}, Priority: {self.priority_score})"

    def to_json(self): # the required output as per my teammate
        return {
            'name':self.name,
            'age':self.age,
            'sex':self.sex,
            'barangay':self.barangay,
            'serious_conditio':self.serious_condition,
            'comorbidities':self.comorbidities,
            'disability':self.disability,
            'transferable_contact':self.transferable_contact
        }

class DataInsertion:
    """Load patients data from a csv file"""

    def load_csv(filepath):
        total_patient = []
        patient_id = 1 # id of the patient

        try:
            with open(filepath, 'r') as f:
                next(f) # first row is the header
                for i in f:
                    csv_data = i.strip().split(',')
                    patient = Patient(patient_id=patient_id,
                                      name=csv_data[0],
                                      age=csv_data[1],
                                      sex=csv_data[2],
                                      barangay=csv_data[3],
                                      serious_condition=csv_data[4],
                                      comorbidities=csv_data[5],
                                      disability=csv_data[6],
                                      transferable_contact=csv_data[7])
                    
                    total_patient.append(patient) 
                    patient_id += 1 # increment the identifier

            print(f'Successfully loaded a total of {len(total_patient)} patients')
            return [p.to_json() for p in total_patient]

        except FileNotFoundError:
            print(f'Error: {filepath} is not found')
            return None
        
    def individual_manual_insert(array, patient_id):                
        patient = Patient(patient_id=patient_id,
                        name=array[0],
                        age=array[1],
                        sex=array[2],
                        barangay=array[3],
                        serious_condition=array[4],
                        comorbidities=array[5],
                        disability=array[6],
                        transferable_contact=array[7])
        print(f'Successfully loaded patient {patient_id}')
        return patient.to_json()

