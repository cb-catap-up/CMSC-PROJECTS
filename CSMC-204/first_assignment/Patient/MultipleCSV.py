from Patient.DataInsertion import DataInsertion
from constants import CSV_PATH
import os


class MultipleCSV(DataInsertion):
    @staticmethod
    def folder_path(folder):
        all_patients = []
        for file in os.listdir(folder):            
            if file.endswith(".csv"):
                full_path = os.path.join(folder, file)
                patients = DataInsertion.load_csv(full_path) # reuse .load_csv 
                all_patients.append(patients)

        print(f"Successfully loaded a total of {len(all_patients)} files")
        return all_patients
         
