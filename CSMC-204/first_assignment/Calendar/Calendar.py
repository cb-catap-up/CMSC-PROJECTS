from Helpers.Helpers import Helpers


class Calendar():
    def __init__(self):
        self.columns_headers = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
        self.number_of_items_per_day = None
        self.patient_time_array = []
        self.dim_array = None
        self.time_start = 8
    
    def display_calendar(self):
        if self.dim_array is None:
            print('no array data')
            return

        two_dim_array = self.dim_array
        two_dim_array_with_headers = []
        two_dim_array_with_headers.append(self.columns_headers)

        for i in two_dim_array:
            item_to_append = []
            for item in i:
                item_to_append.append(item['name'])
            two_dim_array_with_headers.append(item_to_append)
        
        print("\n" + "="*170)
        print(" "*int(120/2) + "PROPOSED PATIENT CALENDAR")
        print("="*170 + '\n')
        
        time_hour = self.time_start
        
        for parent_index,row in enumerate(two_dim_array_with_headers):

            for index, value in enumerate(row):

                if parent_index != 0 and index == 0:
                    time_str = f"{time_hour:02d}:00"
                    print(f"{time_str:<6}   {str(value):<15}", end="")
                    time_hour += 1
                else: 
                    print(f"         {str(value):<16}", end="")
            print("\n")



    def set_array_data(self, items, proposed_patient_number = 4):
        self.dim_array = Helpers.divide_array_by_number(items, proposed_patient_number)
    
    def set_patient_time_array(self):
        two_dim_array = []

        for i in self.dim_array:
            item_to_append = []
            for item in i:
                patient_item = {}
                patient_item['name'] = item['name']
                patient_item['age'] = item['age']
                item_to_append.append(patient_item)
            two_dim_array.append(item_to_append)

        time_hour = self.time_start
        
        
        for parent_index,row in enumerate(two_dim_array):

            for _, value in enumerate(row):
                
                patient_to_append = {}
    
                patient_to_append['name'] = value['name']
                patient_to_append['age'] = value['age']
                patient_to_append['day'] = f"Day {parent_index + 1}"
                patient_to_append['time'] = f"{time_hour:02d}:00"

                time_hour += 1

                self.patient_time_array.append(patient_to_append)

            time_hour = self.time_start


    def get_patient_time_and_day(self, name, age):
        if self.dim_array is None or len(self.patient_time_array) ==0:
            print('no array data')
            return
        for item in self.patient_time_array:
            if (
                str(item['name']) == str(name)
                and int(item['age']) == int(age)
            ):
                return [item['time'], item['day']]
        return ['N/a', 'N/a']