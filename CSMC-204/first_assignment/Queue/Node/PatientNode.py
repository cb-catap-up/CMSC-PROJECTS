from Patient.Patient import Patient

class PatientNode:
    def __init__(self, patient: Patient):
        self.patient = patient
        self.next = None
