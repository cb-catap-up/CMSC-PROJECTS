from Helpers.Helpers import Helpers


class Calendar():
    def __init__(self):
        self.columns_headers = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
        self.number_of_items_per_day = None
        self.patient_time_array = []
        self.dim_array = None
        self.time_start = 8
        self.proposed_patient_number = 8
    
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
        print(" "*int(140/2) + "PROPOSED PATIENT CALENDAR")
        print("="*170 + '\n')
        
        time_hour = self.time_start
        
        # Calculate max width for each column
        col_widths = []

        for col in range(len(two_dim_array_with_headers[0])):
            max_width = max(
                len(str(row[col])) for row in two_dim_array_with_headers
            )
            col_widths.append(max_width + 2) 

        time_width = 6

        for parent_index, row in enumerate(two_dim_array_with_headers):
            for index, value in enumerate(row):
                value_str = str(value)

                if parent_index != 0 and index == 0:
                    time_str = f"{time_hour:02d}:00"
                    print(f"{time_str:<{time_width}} {value_str:<{col_widths[index]}}", end="")
                    time_hour += 1
                else:
                    if index == 0:
                        print(f"{'':<{time_width}} {value_str:<{col_widths[index]}}", end="")
                    else:
                        print(f"      {value_str:<{col_widths[index]}}", end="")
            print('\n')




    def set_array_data(self, items, daily_patient_number = None):
        

        number = self.proposed_patient_number

        if daily_patient_number is not None:

            number = daily_patient_number
            self.proposed_patient_number = number

        # if patient_number exceeds calendar
        show_array = []
        if len(items) > number*7:

            for i in range(number*7):
                show_array.append(items[i])


        self.dim_array = Helpers.divide_array_by_number(show_array, number)
    
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
        
        
        for _,row in enumerate(two_dim_array):

            for row_index, value in enumerate(row):
                
                patient_to_append = {}
    
                patient_to_append['name'] = value['name']
                patient_to_append['age'] = value['age']
                patient_to_append['day'] = f"Day {row_index + 1}"
                patient_to_append['time'] = f"{time_hour:02d}:00"


                self.patient_time_array.append(patient_to_append)
            
            time_hour += 1



    def get_patient_time_and_day(self, name, age, patient_position_in_queue):
        if self.dim_array is None or len(self.patient_time_array) == 0:
            print('no array data')
            return
        if patient_position_in_queue > self.proposed_patient_number*7:
            return ['Not yet scheduled', 'Not yet scheduled']

        for item in self.patient_time_array:
            if (
                str(item['name']) == str(name)
                and int(item['age']) == int(age)
            ):
                return [item['time'], item['day']]
        return ['N/a', 'N/a']
