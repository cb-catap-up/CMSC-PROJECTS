from Queue.Queue import Queue
from Queue.Node.PatientNode import PatientNode
from Patient.Patient import Patient
from constants import QUEUE_PATH
import os
import ast

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
                              disability,
                              transefrable)
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
        # update return queue every addition
        self._update_queue()
    
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
        # update return queue every deletion
        self._update_queue()

    def get_position(self, name, age):
        position = None
        queue_item = self.queue

        try:
            for i in range(len(queue_item)):
                if (
                    str(queue_item[i]['name']) == str(name)
                    and int(queue_item[i]['age']) == int(age)
                ):
                    position = i
                    break
        except:
            return

            
        if position == None:
            print('patient not in queue')
            return
        return position + 1
    
    def search(self, name, age):

        item = {}

        for queue_item in self.queue:
            if (
                str(queue_item['name']).lower() == str(name).lower()
                and int(queue_item['age']) == int(age)
            ):
                item = queue_item
                break

        return item
    
    def display_queue(self, how_many = 3):

        current = self.head
        items = []
        
        print_item = f"\nDisplaying {how_many} sorted nodes (Name: age)\n"
        
        while how_many > 0 and current is not None:
            items.append(f"{current.patient.name}: {current.patient.age}")
            current = current.next
            how_many -= 1
        
        print_item += " -> ".join(items)
        print(print_item)

    def add_queue_from_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                for queue_item in file:
                    queue_object = ast.literal_eval(queue_item)
                    self.enqueue(
                        patient_id=str(queue_object['patient_id']),
                        name=queue_object['name'],
                        age=queue_object['age'],
                        sex=queue_object['sex'],
                        barangay=queue_object['barangay'],
                        serious_condition=queue_object['serious_condition'],
                        comorbidities=queue_object['comorbidities'],
                        disability=queue_object['disability'],
                        transefrable=queue_object['transferable_contact'],
                    )
        except:
            print('error importing queue')

    def _update_queue(self):
        self.queue = []        # deduplication
        current = self.head

        while current:
            
            self.queue.append({
                'patient_id':current.patient.patient_id,
                'name':current.patient.name,
                'age':current.patient.age,
                'sex':current.patient.sex,
                'barangay':current.patient.barangay,
                'serious_condition':current.patient.serious_condition,
                'comorbidities':current.patient.comorbidities,
                'disability':current.patient.disability,
                'transferable_contact':current.patient.transferable_contact
            })
            
            current = current.next

    def get_queue(self):

        return self.queue
    
    def write_queue_to_file(self):

        os.makedirs("database", exist_ok=True)

        with open(QUEUE_PATH, "w") as file:
            for queue_item in self.queue:
                file.write(f"{queue_item}\n")

    def peek(self):
        """
        Show the next patient in queue without removing them
        """
        if self.head is None:
            print("Queue is empty")
            return None
        
        # Return the first patient's information
        next_patient = {
            'name': self.head.patient.name,
            'age': self.head.patient.age,
            'sex': self.head.patient.sex,
        }
        
        print("\n" + "="*50)
        print("NEXT PATIENT IN QUEUE (PEEK)")        
        print(f"Name: {next_patient['name']}")
        print(f"Age: {next_patient['age']}")
        print(f"Sex: {next_patient['sex']}")     
        print("="*50)
        
        return next_patient
    
    def get_head(self):
        """
        Show the head in queue for removal
        """
        if self.head is None:
            print("Queue is empty")
            return None
        
        # Return the first patient's information
        current_patient = {
            'name': self.head.patient.name,
            'age': self.head.patient.age,
            'sex': self.head.patient.sex,
        }
        
        print(f"Name: {current_patient['name']}")
        print(f"Age: {current_patient['age']}")
        print(f"Sex: {current_patient['sex']}")     
        print("="*50)
        
        return current_patient
