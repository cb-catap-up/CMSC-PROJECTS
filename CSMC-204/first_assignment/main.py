from patient import DataInsertion

#### Data insertion via one single file
test = DataInsertion.load_csv('patients_sample.csv')  
print('Sample data')
print(test[0])
print('')

#### Data insertion via manual input
print("--- Enter New Patient Details ---")
user_input = [
    input("Name: "),
    input("Age: "),
    input("Sex: "),
    input("Barangay: "),
    input("Serious Condition (True/False): "),
    input("Comorbidities (True/False): "),
    input("Disability (True/False): "),
    input("Transferable Contact (True/False): ")
]
current_manual_id = 1
new_patient_json = DataInsertion.individual_manual_insert(user_input, current_manual_id)
test.append(new_patient_json)



# .txt = db


# def startApp():
    
#     login = login()

#     patients = getPatients()

#     queue = sortPatients(patients)

#     add_calendar = showCalendar(doctors=3, queue, total_hours_of_caravan = 7, avg_consultation_time = 0.5, )


# results = [
#     {
#         "name": 'test',
#         "last_name": 'test'
#     },
# ]
