from health_db import INFO, save, load

class PatientLogic:
    def __init__(self):
        self.patient_list = load("json")

    def check_duplicate(self, new_patient):
        for patient in self.patient_list:
            if patient.name == new_patient.name and patient.birth_year == new_patient.birth_year:
                return True

        return False #중복이면 T, 중복X 이면 F

    def search_patient(self, ID = None, name = None): #GUI에서 수정
        for patient in self.patient_list:
            if ID is not None:
                if patient.id == ID:
                    return patient.to_dict()

            elif name is not None:
                if patient.name == name:
                    return patient.to_dict()

        return None

    def update_patient(self, search_id, new_height = None, new_weight = None):
        for patient in self.patient_list:
            if patient.id == search_id:
                if new_height is not None: patient.height = new_height
                if new_weight is not None: patient.weight = new_weight
                
                patient.check_bmi()
                save(self.patient_list)

                return True
        return False

    def add_patient(self, name, birth_year, gender, height, weight):
        new_patient = INFO(name, birth_year, gender, height, weight)

        if self.check_duplicate(new_patient):
            return False

        self.patient_list.append(new_patient)
        save(self.patient_list)

        return new_patient.to_dict()

    def delete_patient(self, search_id):
        for idx, patient in enumerate(self.patient_list):
            if patient.id == search_id:
                del self.patient_list[idx]
                save(self.patient_list)
                return True

        return False


        
                

                

