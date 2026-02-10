from Patient.Patient import Patient


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

            print(f'Successfully loaded {len(total_patient)} patients')
            return [p.to_json() for p in total_patient]

        except FileNotFoundError:
            print(f'Error: {filepath} is not found')
            return []
        
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

