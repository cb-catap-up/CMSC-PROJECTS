from Helpers.Helpers import Helpers

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
        self.priority_score = self._priority_score()

    def __repr__(self): # for display purposes
        return f"Patient(ID: {self.patient_id}, Name: {self.name}, Priority: {self.priority_score})"

    def to_json(self): # the required output as per my teammate
        return {
            'patient_id':self.patient_id,
            'name':self.name,
            'age':self.age,
            'sex':self.sex,
            'barangay':self.barangay,
            'serious_condition':self.serious_condition,
            'comorbidities':self.comorbidities,
            'disability':self.disability,
            'transferable_contact':self.transferable_contact
        }
    def _priority_score(self):

        total_score = 0

        if Helpers.convert_true_or_false_string_to_boolean(str(self.serious_condition)):
            total_score += 10
        if Helpers.convert_true_or_false_string_to_boolean(str(self.comorbidities)):
            total_score += 10
        if Helpers.convert_true_or_false_string_to_boolean(str(self.disability)):
            total_score += 10
        if Helpers.convert_true_or_false_string_to_boolean(str(self.transferable_contact)):
            total_score += 5
        if int(self.age) < 12:
            total_score += 5
        if int(self.age) > 60:
            total_score += 10

        return total_score

    
