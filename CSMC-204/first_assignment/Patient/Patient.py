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
        
        # self.priority_score = 0
        # self.scheduled_date = None
        # self.scheduled_time = None
        # self.queue_position = None

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
