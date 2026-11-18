from health_db import INFO, save, load

class PatientLogic:
    def __init__(self):
        self.patient_list = load("json")

    def check_duplicate(self, patient_list):
        pass
