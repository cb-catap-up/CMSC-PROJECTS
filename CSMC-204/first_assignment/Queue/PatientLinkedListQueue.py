from Queue.Queue import Queue
from Queue.Node.PatientNode import PatientNode
from Patient.Patient import Patient

class PatientLinkedListQueue(Queue):
    def __init__(self):
        super().__init__() 
        self.rear = None

    def enqueue(self, 
                patient_id: str,
                name : str, 
                age: int,
                sex: str, 
                barangay: str,
                serious_condition: bool,
                comorbidities: bool,
                disability: bool,
                transefrable: bool):
        
        new_patient = Patient(patient_id,
                              name,
                              age,
                              sex,
                              barangay,
                              serious_condition,
                              comorbidities,
                              disability,transefrable)
        new_patient_node = PatientNode(new_patient)
        
        if self.head is None and self.rear is None:
            self.head = new_patient_node
            self.rear = new_patient_node
        else:

            # current item
            current_item = self.head

            # if item is bigger than head
            if new_patient_node.patient.priority_score > current_item.patient.priority_score:
                new_patient_node.next = self.head
                self.head = new_patient_node
                return
            # traverse list until a lower score is found
            while (
                current_item.next is not None and
                new_patient_node.patient.priority_score
                <= current_item.next.patient.priority_score
            ):
                # traverse list
                current_item = current_item.next
            # insert item
            new_patient_node.next = current_item.next
            current_item.next = new_patient_node

            # Update rear if inserted at end
            if new_patient_node.next is None:
                self.rear = new_patient_node
    
    def dequeue(self, number_to_remove=1):
        if self.head is None:
            print('Queue is empty')
            return
        # progress node
        for _ in range(number_to_remove):
            if self.head is None:
                break
            self.head = self.head.next
            if self.head is None:
                self.rear = None
    
    def display_queue(self):
        current = self.head

        print_item = ""

        while current:
            if current.next is not None:
                print_item += f"{current.patient.name}: {current.patient.age} -> "
            else:
                print_item += f"{current.patient.name}: {current.patient.age}"

            current = current.next

        print(print_item)